import cpi
def main():

    """
    The expected output of this test script is:
    Latest available year in CPI data: 2023 -- This print should give the previous year from when you run it, as the data only exists once a year is completed.

    12643.24 is the revenue, and 126432.37 is the budget, adjusted for inflation
    """
    
    rev = 1000
    budget = 10000

    year = 1950
    current_year = 2023



    rev = round(cpi.inflate(rev, year, to=current_year), 2)
    budget = round(cpi.inflate(budget, year, to=current_year), 2)

    print(f"Latest available year in CPI data: {cpi.LATEST_YEAR}")


    print(f"{rev} is the revenue, and {budget} is the budget, adjusted for inflation")
main()
