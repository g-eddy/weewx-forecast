# installer for the forecast extension
# Copyright 2014-2020 Matthew Wall
# Distributed under the terms of the GNU Public License (GPLv3)

from weecfg.extension import ExtensionInstaller

def loader():
    return ForecastInstaller()

class ForecastInstaller(ExtensionInstaller):
    def __init__(self):
        super(ForecastInstaller, self).__init__(
            version="3.4.0b1",
            name='forecast',
            description='Generate and display weather and tide forecasts.',
            author="Matthew Wall",
            author_email="mwall@users.sourceforge.net",
            archive_services=['user.forecast.ZambrettiForecast',
                              'user.forecast.NWSForecast',
                              'user.forecast.WUForecast',
                              'user.forecast.OWMForecast',
                              'user.forecast.UKMOForecast',
                              'user.forecast.AerisForecast',
                              'user.forecast.WWOForecast',
                              'user.forecast.DSForecast',
                              'user.forecast.XTideForecast'],
            config={
                'Forecast': {
                    'data_binding': 'forecast_binding',
                    'XTide': {
                        'location': 'INSERT_LOCATION_HERE (e.g., Boston)'},
                    'Zambretti': {
                        'hemisphere': 'NORTH'},
                    'NWS': {
                        'lid': 'INSERT_LOCATION_ID_HERE (e.g., MAZ014)',
                        'foid': 'INSERT_FORECAST_OFFICE_ID_HERE (e.g., BOX)'},
                    'WU': {
                        'api_key': 'INSERT_WU_API_KEY_HERE'},
                    'OWM': {
                        'api_key': 'INSERT_OWM_API_KEY_HERE'},
                    'UKMO': {
                        'api_key': 'INSERT_UKMO_API_KEY_HERE',
                        'location': 'INSERT_UK_LOCATION_HERE'},
                    'Aeris': {
                        'client_id': 'INSERT_AERIS_CLIENT_ID_HERE',
                        'client_secret': 'INSERT_AERIS_CLIENT_SECRET_HERE'},
                    'WWO': {
                        'api_key': 'INSERT_WWO_API_KEY_HERE'},
                    'DS': {
                        'api_key': 'INSERT_DS_API_KEY_HERE'}},
                'DataBindings': {
                    'forecast_binding': {
                        'database': 'forecast_sqlite'}},
                'Databases': {
                    'forecast_sqlite': {
                        'database_name': 'forecast.sdb',
                        'database_type': 'SQLite'}},
                'StdReport': {
                    'forecast': {
                        'skin': 'forecast',
                        'HTML_ROOT': 'forecast'}}},
            files=[('bin/user',
                    ['bin/user/forecast.py']),
                   ('skins/compare',
                    ['skins/compare/skin.conf',
                     'skins/compare/index.html.tmpl']),
                   ('skins/forecast',
                    ['skins/forecast/skin.conf',
                     'skins/forecast/forecast.css',
                     'skins/forecast/forecast-periods.html.tmpl',
                     'skins/forecast/forecast_compact.css',
                     'skins/forecast/forecast_compact.inc',
                     'skins/forecast/forecast_iconic.css',
                     'skins/forecast/forecast_iconic.inc',
                     'skins/forecast/forecast_strip.css',
                     'skins/forecast/forecast_strip.inc',
                     'skins/forecast/forecast_table.css',
                     'skins/forecast/forecast_table.inc',
                     'skins/forecast/compact.html.tmpl',
                     'skins/forecast/iconic.html.tmpl',
                     'skins/forecast/iconic-horizontal.html.tmpl',
                     'skins/forecast/index.html.tmpl',
                     'skins/forecast/multiple-strips.html.tmpl',
                     'skins/forecast/multiple-tables.html.tmpl',
                     'skins/forecast/single-strip.html.tmpl',
                     'skins/forecast/single-strip-vertical.html.tmpl',
                     'skins/forecast/single-table.html.tmpl',
                     'skins/forecast/tides.html.tmpl',
                     'skins/forecast/zambretti.html.tmpl']),
                   ('skins/forecast/icons',
                    ['skins/forecast/icons/AF.png',
                     'skins/forecast/icons/B1.png',
                     'skins/forecast/icons/B1n.png',
                     'skins/forecast/icons/B2.png',
                     'skins/forecast/icons/B2n.png',
                     'skins/forecast/icons/BD.png',
                     'skins/forecast/icons/BK.png',
                     'skins/forecast/icons/BKn.png',
                     'skins/forecast/icons/BS.png',
                     'skins/forecast/icons/CL.png',
                     'skins/forecast/icons/CLn.png',
                     'skins/forecast/icons/E.png',
                     'skins/forecast/icons/F+.png',
                     'skins/forecast/icons/F.png',
                     'skins/forecast/icons/FW.png',
                     'skins/forecast/icons/FWn.png',
                     'skins/forecast/icons/H.png',
                     'skins/forecast/icons/K.png',
                     'skins/forecast/icons/N.png',
                     'skins/forecast/icons/NE.png',
                     'skins/forecast/icons/NW.png',
                     'skins/forecast/icons/OV.png',
                     'skins/forecast/icons/OVn.png',
                     'skins/forecast/icons/PF+.png',
                     'skins/forecast/icons/PF.png',
                     'skins/forecast/icons/S.png',
                     'skins/forecast/icons/SC.png',
                     'skins/forecast/icons/SCn.png',
                     'skins/forecast/icons/SE.png',
                     'skins/forecast/icons/SW.png',
                     'skins/forecast/icons/W.png',
                     'skins/forecast/icons/blizzard.png',
                     'skins/forecast/icons/drizzle.png',
                     'skins/forecast/icons/flag-yellow.png',
                     'skins/forecast/icons/flag.png',
                     'skins/forecast/icons/flurries.png',
                     'skins/forecast/icons/frzngdrzl.png',
                     'skins/forecast/icons/moon.png',
                     'skins/forecast/icons/moonphase.png',
                     'skins/forecast/icons/moonrise.png',
                     'skins/forecast/icons/moonriseset.png',
                     'skins/forecast/icons/moonset.png',
                     'skins/forecast/icons/pop.png',
                     'skins/forecast/icons/rain.png',
                     'skins/forecast/icons/raindrop.png',
                     'skins/forecast/icons/rainshwrs.png',
                     'skins/forecast/icons/raintorrent.png',
                     'skins/forecast/icons/sleet.png',
                     'skins/forecast/icons/snow.png',
                     'skins/forecast/icons/snowflake.png',
                     'skins/forecast/icons/snowshwrs.png',
                     'skins/forecast/icons/sprinkles.png',
                     'skins/forecast/icons/sun.png',
                     'skins/forecast/icons/sunmoon.png',
                     'skins/forecast/icons/sunrise.png',
                     'skins/forecast/icons/sunriseset.png',
                     'skins/forecast/icons/sunset.png',
                     'skins/forecast/icons/tE.png',
                     'skins/forecast/icons/tENE.png',
                     'skins/forecast/icons/tESE.png',
                     'skins/forecast/icons/tN.png',
                     'skins/forecast/icons/tNE.png',
                     'skins/forecast/icons/tNNE.png',
                     'skins/forecast/icons/tNNW.png',
                     'skins/forecast/icons/tNW.png',
                     'skins/forecast/icons/tS.png',
                     'skins/forecast/icons/tSE.png',
                     'skins/forecast/icons/tSSE.png',
                     'skins/forecast/icons/tSSW.png',
                     'skins/forecast/icons/tSW.png',
                     'skins/forecast/icons/tW.png',
                     'skins/forecast/icons/tWNW.png',
                     'skins/forecast/icons/tWSW.png',
                     'skins/forecast/icons/thermometer-blue.png',
                     'skins/forecast/icons/thermometer-dewpoint.png',
                     'skins/forecast/icons/thermometer-red.png',
                     'skins/forecast/icons/thermometer.png',
                     'skins/forecast/icons/triangle-down.png',
                     'skins/forecast/icons/triangle-right.png',
                     'skins/forecast/icons/tstms.png',
                     'skins/forecast/icons/water.png']),
                   ]
            )
