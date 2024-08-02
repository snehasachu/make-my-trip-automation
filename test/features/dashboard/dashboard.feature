Feature: Make my trip Dashboard Page Tests

  @dashboard @regression_p0
  Scenario: Planning a trip internationally feature validation
    Given user is on dashboard page
    When user in dahsboard verify make my trip title header present
    Then select from as Bangalore
    And select Planning a trip internationally
    And select to as Dubai
    And click on departure field
    And click on the search button
    And Retrieve all the dates with the flight price
    And user navigates to make my trip home page

  @dashboard @smoke
  Scenario: Navigate to make My Trip and verify the objects in the landing page
    Given user is on dashboard page
    When user in dahsboard verify make my trip title header present
    Then verify Flights header present
    And click on flights header
    And verify Hotels header present
    And verify HomeStays and villas header present
    And verify Holiday packages header present
    And verify Trains header present
    And verify Buses header present
    And verify Cabs header present
    And verify Forex card and Currency header present
    And verify Travel insurance header present
    And verify from city drop down box
    And verify to city drop down box
    And verify Planning a trip internationally option in drop down box
    And verify Travel date header present
    And verify Search button present
#    And verify Offers header present

  @dashboard @smoke
  Scenario: Navigation to International Trip Planning Page and verify the objects in the landing page
    Given user is on dashboard page
    When user in dahsboard verify make my trip title header present
#    Then select from as Bangalore
    Then refresh the my trip page
    And select Planning a trip internationally
    And verify Flights header present
    And verify Hotels header present
    And verify HomeStays and villas header present
    And verify Holiday packages header present
    And verify Trains header present
    And verify Buses header present
    And verify Cabs header present
    And verify Forex card and Currency header present
    And verify Travel insurance header present
    And verify more header present
    And user navigates to make my trip home page
#
  @dashboard @smoke
  Scenario: Navigation to International Trip Planning Page and verify the dropdowns and filters in the landing page
    Given user is on dashboard page
    When user in dahsboard verify make my trip title header present
#    Then select from as Bangalore
    Then refresh the my trip page
    And click on flights header
    And select Planning a trip internationally
    And verify and click trip type drop down
    And verify and click from city drop down
    And verify and click to city drop down
    And verify departure drop down
    And verify anytime and apply buttons in departure dialogue box
    And click on the search button
    And verify international trip filters present
    And verify flights from bangaluru to header present
    And user navigates to make my trip home page
#
  @dashboard @smoke @test6
  Scenario: Navigation to International Trip Planning Page and verify the map functionalities
    Given user is on dashboard page
    When user in dahsboard verify make my trip title header present
    Then refresh the my trip page
    And click on flights header
#    Then select from as Bangalore
    And select Planning a trip internationally
    And verify map button present
    And verify satellite button present
    And verify Google image logo is present on the map
    And verify open Street View option present
    And verify Zoom In button is present and clickable
    And verify Zoom Out button is present and clickable
    And verify Toggle fullscreen view button is present and clickable
    And user navigates to make my trip home page

  @dashboard @test6
  Scenario: Navigate to International Trip Planning Page and very sort by drop down
    Given user is on dashboard page
    When user in dahsboard verify make my trip title header present
    Then refresh the my trip page
    And click on flights header
    And select Planning a trip internationally
    And verify and click sort by drop down
    And select sort by price from drop down
    And select sort by popularity from drop down
    And select dort by duration from drop down
    And user navigates to make my trip home page

  @dashboard @smoke @test6
  Scenario: Navigation to International Trip Planning Page and verify the round trip
    Given user is on dashboard page
    When user in dahsboard verify make my trip title header present
    Then refresh the my trip page
    And click on flights header
    And select Planning a trip internationally
    And select round trip from trip type dropdown
    And verify departure autopopulated to anytime 7 days
    And user navigates to make my trip home page

  @dashboard
  Scenario: Navigate to International Trip Planning Page and apply multiple filters
    Given user is on dashboard page
    When user in dahsboard verify make my trip title header present
    Then refresh the my trip page
    And click on flights header
    And select Planning a trip internationally
    And select multiple filters from stops
    And verify too many filters error in page
    And select clear all filters option
    And user navigates to make my trip home page

  @dashboard @regression_p0
  Scenario: Verify international trip planning with no flights found
    Given user is on dashboard page
    When user in dahsboard verify make my trip title header present
    Then select from as Bangalore
    And select Planning a trip internationally
    And select to city as Karachi
    And click on departure field
    And click on the search button
    And verify the error page with no flights found message
    And select go back button
    And user navigates to make my trip home page

  @dashboard @regression_p0 @test8
  Scenario: Verify international trip planning and price sorting functionality on dashboard
    Given user is on dashboard page
    When user in dahsboard verify make my trip title header present
    Then select from as Bangalore
    And select Planning a trip internationally
    And verify and click sort by drop down
    And select sort by price from drop down
    And verify the prices are in sorted or not
    And user navigates to make my trip home page
