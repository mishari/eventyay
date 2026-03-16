import logging
from urllib.parse import quote

import requests
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.cache import cache
from django.http import JsonResponse
from django.views.generic.base import View

from eventyay.base.settings import GlobalSettingsObject

logger = logging.getLogger(__name__)


class GeoCodeView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        q = self.request.GET.get('q')
        cd = cache.get('geocode:{}'.format(q))
        if cd:
            return JsonResponse({'success': True, 'results': cd}, status=200)

        gs = GlobalSettingsObject()
        try:
            if gs.settings.opencagedata_apikey:
                res = self._use_opencage(q)
            elif gs.settings.mapquest_apikey:
                res = self._use_mapquest(q)
            else:
                return JsonResponse({'success': False, 'results': []}, status=200)
        except requests.RequestException:
            logger.exception('Geocoding failed')
            return JsonResponse({'success': False, 'results': []}, status=200)

        cache.set('geocode:{}'.format(q), res, timeout=3600 * 6)
        return JsonResponse({'success': True, 'results': res}, status=200)

    def _use_opencage(self, q):
        gs = GlobalSettingsObject()

        response = requests.get(
            'https://api.opencagedata.com/geocode/v1/json?q={}&key={}'.format(quote(q), gs.settings.opencagedata_apikey),
            timeout=30,
        )
        response.raise_for_status()
        d = response.json()
        res = [
            {
                'formatted': result['formatted'],
                'lat': result['geometry']['lat'],
                'lon': result['geometry']['lng'],
            }
            for result in d['results']
        ]
        return res

    def _use_mapquest(self, q):
        gs = GlobalSettingsObject()

        response = requests.get(
            'https://www.mapquestapi.com/geocoding/v1/address?location={}&key={}'.format(
                quote(q), gs.settings.mapquest_apikey
            ),
            timeout=30,
        )
        response.raise_for_status()
        d = response.json()
        res = [
            {
                'formatted': q,
                'lat': result['locations'][0]['latLng']['lat'],
                'lon': result['locations'][0]['latLng']['lng'],
            }
            for result in d['results']
        ]
        return res
