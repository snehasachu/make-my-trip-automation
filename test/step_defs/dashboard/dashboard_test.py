from pypom import Page
from pytest_bdd import scenarios, given, when, then
from test.pages.dashboard.dashboard_page import DashboardPage
from conftest import web_driver
import time

scenarios('../../features/dashboard/dashboard.feature')
dashboard_page = DashboardPage(web_driver)

@given("user is on dashboard page", target_fixture="user_on_dashboard_page")
def user_is_on_dashboard() -> Page:
    time.sleep(30)
    return dashboard_page

@when("user in dashboard verify make my trip title header present")
def verify_title_header():
    assert dashboard_page.check_title_header_present()

@then("select from as Bangalore")
def verify_flights_from_option():
    dashboard_page.verify_flights_from()

@then("refresh the my trip page")
def refresh_log_center_page():
    dashboard_page.refresh_page()

@then('user navigates to make my trip home page')
def user_navigates_to_make_my_trip_home_page():
    dashboard_page.click_on_dashboard_page_header()

@then("select Planning a trip internationally")
def select_planning_trip_internationally():
    dashboard_page.select_international_trips()

@then("select to as Dubai")
def verify_flights_to_option():
    dashboard_page.verify_flights_to_()

@then("select to city as Karachi")
def verify_flights_to_karachi():
    dashboard_page.verify_flights_to_karachi()

@then("click on departure field")
def click_departure_field():
    dashboard_page.click_departure_field()

@then("click on the search button")
def click_search_button():
    dashboard_page.click_search_button()

@then("Retrieve all the dates with the flight price")
def verify_all_flight_price():
    assert dashboard_page.verify_all_flight_price()

@then('verify Flights header present')
def verify_flights_header_present():
    assert dashboard_page.verify_flights_header_present()

@then('select go back button')
def select_go_back_button():
    dashboard_page.select_go_back_button()

@then('verify the error page with no flights found message')
def verify_error_no_flights():
    assert dashboard_page.verify_error_no_flights()

@then('click on flights header')
def click_flights_header():
    dashboard_page.click_flights_header()

@then('verify Hotels header present')
def verify_hotels_header_present():
    assert dashboard_page.verify_hotels_header_present()

@then('verify HomeStays and villas header present')
def verify_homestays_header_present():
    assert dashboard_page.verify_homestays_header_present()

@then('verify Holiday packages header present')
def verify_holiday_packages_header_present():
    assert dashboard_page.verify_holiday_packages_header_present()

@then('verify Trains header present')
def verify_trains_header_present():
    assert dashboard_page.verify_trains_header_present()

@then('verify Buses header present')
def verify_buses_header_present():
    assert dashboard_page.verify_buses_header_present()

@then('verify Cabs header present')
def verify_cabs_header_present():
    assert dashboard_page.verify_cabs_header_present()

@then('verify Forex card and Currency header present')
def verify_currency_header_present():
    assert dashboard_page.verify_currency_header_present()

@then('verify Travel insurance header present')
def verify_travel_insurance_header_present():
    assert dashboard_page.verify_travel_insurance_header_present()

@then('verify from city drop down box')
def verify_from_city_dropdown_present():
    assert dashboard_page.verify_from_city_dropdown_present()

@then('verify to city drop down box')
def verify_to_city_dropdown_present():
    assert dashboard_page.verify_to_city_dropdown_present()

@then('verify Planning a trip internationally option in drop down box')
def verify_trip_international_option_present():
    assert dashboard_page.verify_trip_international_option_present()

@then('verify Travel date header present')
def verify_travel_date_header_present():
    assert dashboard_page.verify_travel_date_header_present()

@then('verify Search button present')
def verify_search_button_present():
    assert dashboard_page.verify_search_button_present()

@then('verify Offers header present')
def verify_offers_header_present():
    assert dashboard_page.verify_offers_header_present()

@then('verify more header present')
def verify_more_header_present():
    assert dashboard_page.verify_more_header_present()

@then('verify and click trip type drop down')
def verify_trip_type_header_present():
    assert dashboard_page.verify_trip_type_header_present()

@then('verify map button present')
def verify_map_button():
    dashboard_page.verify_map_button()

@then('verify and click from city drop down')
def verify_from_city_drop_down():
    assert dashboard_page.verify_from_city_drop_down()
    dashboard_page.click_from_city_drop_down()

@then('verify and click to city drop down')
def verify_to_city_drop_down():
    assert dashboard_page.verify_to_city_drop_down()
    dashboard_page.click_to_city_drop_down()

@then('verify departure drop down')
def verify_departure():
    assert dashboard_page.verify_departure()

@then('verify anytime and apply buttons in departure dialogue box')
def verify_departure_box_buttons():
    assert dashboard_page.verify_departure_box_buttons()

@then('verify map button present')
def verify_map_buttons():
    assert dashboard_page.verify_map_buttons()

@then('verify satellite button present')
def verify_satellite_buttons():
    assert dashboard_page.verify_satellite_buttons()

@then('verify Google image logo is present on the map')
def verify_google_logo():
    assert dashboard_page.verify_google_logo()

@then('verify open Street View option present')
def verify_open_street_view_button():
    assert dashboard_page.verify_open_street_view_button()

@then('verify Zoom In button is present and clickable')
def verify_zoom_in_button():
    assert dashboard_page.verify_zoom_in_button()

@then('verify Zoom Out button is present and clickable')
def verify_zoom_out_button():
    assert dashboard_page.verify_zoom_out_button()

@then('verify Toggle fullscreen view button is present and clickable')
def verify_view_fullscreen_button():
    assert dashboard_page.verify_view_fullscreen_button()

@then('verify international trip filters present')
def verify_trip_filters():
    assert dashboard_page.verify_trip_filters()

@then('verify flights from bangaluru to header present')
def verify_flights_from_to_header():
    assert dashboard_page.verify_flights_from_to_header() == "Flights from Bengaluru to"

@then('select round trip from trip type dropdown')
def select_round_trip():
    assert dashboard_page.select_round_trip()

@then('verify departure autopopulated to anytime 7 days')
def verify_anytime_departure():
    assert dashboard_page.verify_anytime_departure()

@then('select multiple filters from stops')
def select_stops_multiple_filters():
    dashboard_page.select_stops_multiple_filters()

@then('verify too many filters error in page')
def verify_too_many_filters():
    assert dashboard_page.verify_too_many_filters()

@then('select clear all filters option')
def select_clear_filter_option():
    dashboard_page.select_clear_filter_option()

@then('verify and click sort by drop down')
def select_sort_by_dropdown():
    dashboard_page.select_sort_by_dropdown()

@then('select sort by price from drop down')
def select_sort_by_price():
    dashboard_page.select_sort_by_price()

@then('select sort by popularity from drop down')
def select_sort_by_popularity():
    dashboard_page.select_sort_by_popularity()

@then('select sort by duration from drop down')
def select_sort_by_duration():
    dashboard_page.select_sort_by_duration()

@then('verify the prices are in sorted or not')
def verify_prices_order():
    assert dashboard_page.verify_prices_order()

@then('verify the durations are in sorted or not')
def verify_durations_order():
    assert dashboard_page.verify_durations_order()