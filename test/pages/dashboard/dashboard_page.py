import time
from pypom import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
import numpy as np
from datetime import datetime
import re

class DashboardPage(Page):
    _title_header = (By.XPATH, "//img[@alt='Make My Trip']")
    home_page_header = (By.XPATH, "(//div[@class='commonHeader'])[1]")
    flights_header = (By.XPATH,"//li[@class='menu_Flights']//span[@data-cy='item-wrapper']")
    hotels_header = (By.XPATH,"//li[@class='menu_Hotels']//span[@data-cy='item-wrapper']")
    homestays_header = (By.XPATH, "//a[@href='https://www.makemytrip.com/homestays/']")
    holidays_header = (By.XPATH, "//a[@href='https://www.makemytrip.com/holidays-india/']")
    trains_header = (By.XPATH, "//li[@class='menu_Trains']//span[@data-cy='item-wrapper']")
    buses_header = (By.XPATH, "//li[@class='menu_Buses']//span[@data-cy='item-wrapper']")
    cabs_header = (By.XPATH, "//li[@class='menu_Cabs']//span[@data-cy='item-wrapper']")
    forex_card_currency_header = (By.XPATH, "//a[@href='https://www.makemytrip.com/forex/']")
    travel_insurance_header = (By.XPATH, "//a[@href='https://www.makemytrip.com/insurance/']")
    from_city_header = (By.XPATH, "//span[normalize-space()='From']")
    trip_city_from_header = (By.XPATH, "//label[normalize-space()='FROM']")
    to_city_header = (By.XPATH, "//span[normalize-space()='To']")
    trip_city_to_header = (By.XPATH, "//label[normalize-space()='TO']")
    departure_header = (By.XPATH, "//span[normalize-space()='Departure']")
    search_button = (By.XPATH, "//a[normalize-space()='Search']")
    anytime_button = (By.XPATH, "//span[@class='active']")
    offers_header = (By.XPATH, "//font[normalize-space()='Offers']")
    more_option_header = (By.XPATH, "//span[@class='itemWrapper headerIcons makeFlex hrtlCenter column moreWrapper']")
    trip_type_header = (By.XPATH,"//label[normalize-space()='TRIP TYPE']")
    round_trip = (By.XPATH,"(//li[@class='list-item'])[1]")
    international_trips_header = (By.XPATH, "//div[@class='makeFlex column intlFlightTile-autosuggest']")
    trip_page_departure_header = (By.XPATH, "//label[normalize-space()='DEPARTURE']")
    date_and_duration = (By.XPATH, "//label[normalize-space()='DATES & DURATION']")
    apply_button = (By.XPATH, "//button[normalize-space()='Apply']")
    trip_page_search_button = (By.XPATH, "//button[normalize-space()='Search']")
    visa_documents_header = (By.XPATH, "//p[normalize-space()='Visa & Documents']")
    flight_duration_header = (By.XPATH, "//p[normalize-space()='Flight Duration']")
    one_way_price = (By.XPATH, "//p[normalize-space()='One Way Price']")
    stops_header = (By.XPATH, "//p[normalize-space()='Stops']")
    popular_filters_header = (By.XPATH, "//p[normalize-space()='Popular Filters']")
    map_button = (By.XPATH, "(//button[normalize-space()='Map'])[1]")
    satellite_button = (By.XPATH, "(//button[normalize-space()='Satellite'])[1]")
    google_logo = (By.XPATH, "//img[@alt='Google']")
    open_street_view = (By.XPATH,"//button[@title='Drag Pegman onto the map to open Street View']")
    zoom_in_button = (By.XPATH,"//button[@title='Zoom in']")
    zoom_out_button = (By.XPATH,"//button[@title='Zoom out']")
    toggle_full_screen = (By.XPATH,"//button[@title='Toggle fullscreen view']")

    @property
    def loaded(self) -> bool:
        self.wait_for_page_to_load()
        return self.is_element_displayed(*self._title_header)

    def check_title_header_present(self):
        tab_xpath = (By.XPATH, "// span[ @class ='commonModal__close']")
        if self.is_element_displayed(*tab_xpath):
            self.find_element(*tab_xpath).click()
        return self.is_element_displayed(*self._title_header)

    def click_on_dashboard_page_header(self):
        self.find_element(*self.home_page_header).click()

    def verify_flights_from(self):
        tab_xpath = (By.XPATH, "//input[@id='fromCity']")
        self.find_element( * tab_xpath).click()
        bangalore_city = (By.XPATH,"//p[normalize-space()='Bengaluru, India']")
        self.find_element( * bangalore_city).click()

    def select_international_trips(self):
        tab_xpath = (By.XPATH, "//input[@id='toCity']")
        self.wait.until(ec.presence_of_element_located(tab_xpath))
        self.find_element(*tab_xpath).click()
        planning_international = (By.XPATH,"//p[@class='makeFlex spaceBetween perfectCenter appendBottom5 cursorPointer']")
        return self.find_element( * planning_international).click()

    def verify_flights_to_(self):
        tab_xpath = (By.XPATH, "//span[@class='value'][normalize-space()='ANYWHERE']")
        self.find_element( * tab_xpath).click()
        to_xpath = (By.XPATH,"(//input[@placeholder='Enter City'])[2]")
        self.wait.until(ec.presence_of_element_located(to_xpath))
        self.find_element(*to_xpath).send_keys("dxb")
        # dubai_city = (By.XPATH,"//*[contains(text(), 'Dubai')]")
        parent_element = self.find_elements(By.CLASS_NAME, "dpcityList")
        # print (parent_element.)
        for element in parent_element:
            if "Dubai" in element.text:
                element.click()
                break
    
    def verify_flights_to_karachi(self):
        tab_xpath = (By.XPATH, "//span[@class='value'][normalize-space()='ANYWHERE']")
        self.find_element( * tab_xpath).click()
        to_xpath = (By.XPATH,"(//input[@placeholder='Enter City'])[2]")
        self.wait.until(ec.presence_of_element_located(to_xpath))
        self.find_element(*to_xpath).send_keys("pak")
        # dubai_city = (By.XPATH,"//*[contains(text(), 'Dubai')]")
        parent_element = self.find_elements(By.CLASS_NAME, "dpcityList")
        # print (parent_element.)
        for element in parent_element:
            if "Karachi" in element.text:
                element.click()
                break

    def refresh_page(self):
        self.driver.refresh()

    def verify_all_flight_price(self):
        # tab_xpath = (By.XPATH, "//div[@id='DAC']")
        tab_xpath = (By.XPATH, "(//div[@id='DXB'])[1]")
        self.find_element( * tab_xpath).click()
        date_xpath = "//div[contains(@class,'tripFareCalList')]"
        elements = self.wait.until(ec.presence_of_all_elements_located((By.XPATH, date_xpath)))

        flight_data = []
        for element in elements:
            text = element.text
            # Assuming the format "Date₹ Price" e.g., "10₹ 35,230"
            parts = text.split('₹')
            if len(parts) == 2:
                date = parts[0].strip()
                price = float(parts[1].strip().replace(',', ''))
                flight_data.append((date, price))
        print(flight_data)
        prices = [price for date, price in flight_data]
        print(prices)

        median_price = np.median(prices)
        print(f"Median Price: {median_price}")

        dates_below_median = [date for date, price in flight_data if price <= median_price]
        print(f"Dates with prices below the median: {dates_below_median}")

        weekend_dates = []
        for date_str in dates_below_median:
            date_obj = datetime.strptime(date_str, '%d').replace(month=12, year=2024)
            if date_obj.weekday() == 5 or date_obj.weekday() == 6:  # 5 is Saturday, 6 is Sunday
                weekend_dates.append((date_str, [price for date, price in flight_data if date == date_str][0]))

        if weekend_dates:
            weekend_dates.sort(key=lambda x: x[1])
            lowest_weekend_date = weekend_dates[0][0]
            print(f"Weekend date with the lowest price: {lowest_weekend_date}")
            lowest_weekend_element = next(el for el in elements if lowest_weekend_date in el.text)
            lowest_weekend_element.click()
        else:
            flight_data.sort(key=lambda x: x[1])
            lowest_price_date = flight_data[0][0]
            print(f"Date with the lowest price: {lowest_price_date}")
            lowest_price_element = next(el for el in elements if lowest_price_date in el.text)
            lowest_price_element.click()

        check_xpath = (By.XPATH,
                       "//body/div[@id='root']/div/div/div[@class='flightIntlDestBody']/div[@class='CalendarFareSection active']/div/div/div/div[1]/div[1]/div[1]")
        check_elements = self.driver.find_elements(*check_xpath)
        return check_elements and check_elements[0].is_displayed()

    def verify_flights_header_present(self):
        return self.is_element_present(*self.flights_header)
    
    def verify_error_no_flights(self):
        error_xpath = (By.XPATH, "//p[@class='error-title']")
        return self.is_element_present(*error_xpath)

    def click_flights_header(self):
        self.find_element(*self.flights_header).click()

    def select_go_back_button(self):
        go_back_button = (By.XPATH, "//a[normalize-space()='Go Back']")
        self.wait.until(ec.presence_of_element_located(go_back_button))
        self.find_element(*go_back_button).click()

    def verify_hotels_header_present(self):
        return self.is_element_present(*self.hotels_header)

    def verify_homestays_header_present(self):
        return self.is_element_present(*self.homestays_header)

    def verify_holiday_packages_header_present(self):
        return self.is_element_present(*self.holidays_header)

    def verify_trains_header_present(self):
        return self.is_element_present(*self.trains_header)

    def verify_buses_header_present(self):
        return self.is_element_present(*self.buses_header)

    def verify_cabs_header_present(self):
        return self.is_element_present(*self.cabs_header)

    def verify_currency_header_present(self):
        return self.is_element_present(*self.forex_card_currency_header)

    def verify_travel_insurance_header_present(self):
        return self.is_element_present(*self.travel_insurance_header)

    def verify_from_city_dropdown_present(self):
        return self.is_element_present(*self.from_city_header)

    def verify_to_city_dropdown_present(self):
        return self.is_element_present(*self.to_city_header)

    def verify_trip_international_option_present(self):
        self.find_element(*self.to_city_header).click()
        return self.is_element_present(*self.international_trips_header)

    def verify_travel_date_header_present(self):
        return self.is_element_present(*self.departure_header)

    def verify_search_button_present(self):
        return self.is_element_present(*self.search_button)

    def verify_offers_header_present(self):
        return self.is_element_present(*self.offers_header)

    def click_departure_field(self):
        departure_xpath = (By.XPATH, "//label[normalize-space()='DEPARTURE']")
        self.find_element( * departure_xpath).click()
        departure_month = (By.XPATH,"//span[normalize-space()='December, 2024']")
        self.find_element( * departure_month).click()
        apply_button = (By.XPATH, "//button[normalize-space()='Apply']")
        self.find_element(*apply_button).click()
    #
    def click_search_button(self):
        search_button = (By.XPATH, "//button[normalize-space()='Search']")
        self.find_element(*search_button).click()
        time.sleep(10)

    def verify_more_header_present(self):
        return self.is_element_present(*self.more_option_header)

    def verify_map_buttons(self):
        self.wait.until(ec.presence_of_element_located(self.map_button))
        return self.is_element_present(*self.map_button)

    def verify_satellite_buttons(self):
        self.wait.until(ec.presence_of_element_located(self.satellite_button))
        return self.is_element_present(*self.satellite_button)

    def verify_google_logo(self):
        self.wait.until(ec.presence_of_element_located(self.google_logo))
        return self.is_element_present(*self.google_logo)

    def verify_zoom_in_button(self):
        self.wait.until(ec.presence_of_element_located(self.zoom_in_button))
        self.find_element(*self.zoom_in_button).click()
        return self.is_element_present(*self.zoom_in_button)

    def verify_zoom_out_button(self):
        self.wait.until(ec.presence_of_element_located(self.zoom_out_button))
        self.find_element(*self.zoom_out_button).click()
        return self.is_element_present(*self.zoom_out_button)

    def verify_view_fullscreen_button(self):
        self.wait.until(ec.presence_of_element_located(self.toggle_full_screen))
        self.find_element(*self.toggle_full_screen).click()
        self.find_element(*self.toggle_full_screen).click()
        return self.is_element_present(*self.toggle_full_screen)

    def verify_open_street_view_button(self):
        self.wait.until(ec.presence_of_element_located(self.open_street_view))
        return self.is_element_present(*self.open_street_view)

    def verify_trip_type_header_present(self):
        return self.is_element_present(*self.trip_type_header)

    def verify_from_city_drop_down(self):
        return self.is_element_present(*self.trip_city_from_header)

    def click_from_city_drop_down(self):
        self.find_element(*self.trip_city_from_header).click()

    def verify_to_city_drop_down(self):
        return self.is_element_present(*self.trip_city_to_header)

    def click_to_city_drop_down(self):
        self.find_element(*self.trip_city_to_header).click()

    def verify_departure(self):
        return self.is_element_present(*self.trip_page_departure_header)

    def verify_departure_box_buttons(self):
        return self.is_element_present(*self.anytime_button) and self.is_element_present(*self.apply_button)

    def verify_trip_filters(self):
        headers = [self.visa_documents_header, self.flights_header, self.one_way_price,self.stops_header,self.popular_filters_header]
        return all(self.is_element_present(*header) for header in headers)

    def verify_flights_from_to_header(self):
        xpath = (By.XPATH, "//p[@class='font18 blackFont flexOne']")
        element = self.find_element(*xpath)
        return element.text

    def select_round_trip(self):
        self.find_element(*self.trip_type_header).click()
        self.find_element(*self.round_trip).click()
        return self.is_element_present(*self.round_trip)

    def verify_anytime_departure(self):
        anytime_xpath = (By.XPATH, "//span[normalize-space()='Anytime , 7 Days']")
        return self.is_element_present(*anytime_xpath)

    def select_stops_multiple_filters(self):
        non_stop_xpath = (By.XPATH, "(//input[@id='destinationPickerHorizontalItem'])[4]")
        self.is_element_present(*non_stop_xpath).click()
        one_stop_xpath = (By.XPATH, "(//input[@id='destinationPickerHorizontalItem'])[5]")
        self.is_element_present(*one_stop_xpath).click()

    def verify_too_many_filters(self):
        too_many_filters_icon = (By.XPATH, "//span[@class='multipleFilterIcon']")
        self.wait.until(ec.presence_of_element_located(too_many_filters_icon))
        return self.is_element_present(*too_many_filters_icon)
    
    def select_clear_filter_option(self):
        clear_filters_icon = (By.XPATH, "(//span[@class='linkText boldFont font12'])[1]")
        self.is_element_present(*clear_filters_icon).click()
        time.sleep(10)

    def select_sort_by_dropdown(self):
        sort_drop_down = (By.XPATH, "//div[@class='selectValue']")
        self.is_element_present(*sort_drop_down).click()

    def select_sort_by_price(self):
        sort_price = (By.XPATH, "//li[normalize-space()='Price']")
        self.is_element_present(*sort_price).click()

    def select_sort_by_popularity(self):
        sort_drop_down = (By.XPATH, "//div[@class='selectValue']")
        if self.is_element_displayed(*sort_drop_down):
            self.find_element(*sort_drop_down).click()
        sort_popularity = (By.XPATH, "//li[normalize-space()='Popularity']")
        self.is_element_present(*sort_popularity).click()

    def select_sort_by_duration(self):
        sort_drop_down = (By.XPATH, "//div[@class='selectValue']")
        if self.is_element_displayed(*sort_drop_down):
            self.find_element(*sort_drop_down).click()
        sort_duration = (By.XPATH, "//li[normalize-space()='Duration']")
        self.is_element_present(*sort_duration).click()

    def verify_prices_order(self):
        price_elements = self.find_elements(By.CLASS_NAME, "priceDp")
        amounts = []
        for element in price_elements:
            price_text = element.text
            match = re.search(r'₹\s?([\d,]+)', price_text)
            if match:
                amount = int(match.group(1).replace(',', ''))
                amounts.append(amount)
        is_sorted = all(amounts[i] <= amounts[i + 1] for i in range(len(amounts) - 1))
        return is_sorted
    
    def verify_durations_order(self):
        duration_elements = self.find_elements(By.CLASS_NAME, 'darkText')
        durations = []
        for element in duration_elements:
            duration_text = element.text
            days = 0           
            hours = 0
            minutes = 0
        days_match = re.search(r'(\d+)\s*day[s]?', duration_text)
        if days_match:
            days = int(days_match.group(1))
        
        hours_match = re.search(r'(\d+)\s*hr[s]?', duration_text)
        if hours_match:
            hours = int(hours_match.group(1))
        
        minutes_match = re.search(r'(\d+)\s*min[s]?', duration_text)
        if minutes_match:
            minutes = int(minutes_match.group(1))
        
        total_minutes = days * 24 * 60 + hours * 60 + minutes
        durations.append(total_minutes)
        print(durations)
        is_sorted = all(durations[i] <= durations[i + 1] for i in range(len(durations) - 1))
        return is_sorted



