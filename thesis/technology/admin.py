from django.contrib import admin
#from .models import Gasheater
#from .models import Heatpump, Parameters
from .models import Sfh, Mfh,Commercial,Tos, BuildingProfile

class EntryAdmin(admin.ModelAdmin):
    list_display = ('technology', 'model')
    list_filter = ['model']


#class SfhAdmin(admin.ModelAdmin):
    #list_display = ('numofpersons', 'electricalenergyconsumption', 'dhwenergyconsumption','buildingsize')
    #list_filter = ['numofpersons']



#class MfhAdmin(admin.ModelAdmin):
    #list_display = ('numofdwellings', 'thermalbuildingstandard', 'electricalenergyconsumption', 'dhwenergyconsumption','buildingsize')
    #list_filter = ['numofdwellings']

#class Commercialdmin(admin.ModelAdmin):
    #list_display = ('electricalenergyconsumption', 'electricalenergyprofiletype', 'thermalbuildingtype','buildingsize')
    #list_filter = ['electricalenergyconsumption']

# class Economicadmin(admin.ModelAdmin):
#     list_display = ('electricity_fixed_costs_per_year', 'electricity_costs_per_kWh', 'electricity_feed_in_tariff_chp', 'electricity_feed_in_tariff_for_photovoltaic', 'gas_fixed_costs_per_year', 'gas_costs_per_kwh', 'battery_costs_perkW_inverter_power','battery_costs_perkWh_capacity', 'battery_costs_for_maintenance_and_operations','battery_lifetime', 'hydrogen_costs_perkw_electrolyseur_power','hydrogen_costs_perkw_fuel_cellpower','hydrogen_costsperkWh_hydrogencapacity','hydrogen_costs_for_maintenance_and_operations','hydrogen_lifetime','hydrogen_interest_rate')
#     list_filter = ['electricity_fixed_costs_per_year']


#class Tosadmin(admin.ModelAdmin):
 #   list_display = ('installedgenpower', 'azimut', 'elevation', 'ratedinverterpower', 'chpcombinedheatpower', 'chpoperationstrategy', 'heatpumptechnology', 'heatpumpmodel', 'bsfeedinlimitation', 'bsusablecapacity', 'bsratedpower', 'hsusablecapacity', 'hsratedpower', 'elvehiclesdistance')
  #  list_filter = ['chpcombinedheatpower ']

#class BuildingProfile(admin.ModelAdmin):
 #   list_display = ('technology','numofpersons', 'electricalenergyconsumption', 'energyconsumption', 'buildingsize')
  #  list_filter = ['numofpersons']

# Register your models here.
#admin.site.register(Heatpump)
#admin.site.register(Sfh)
#admin.site.register(Mfh)
#admin.site.register(Commercial)
admin.site.register(Tos)
admin.site.register(BuildingProfile)


#admin.site.register(Gasheater)
#admin.site.register(Mynumber, MynumberAdmin)
admin.site.site_header = "Jülich Dashboard"

