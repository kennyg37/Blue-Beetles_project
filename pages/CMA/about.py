
#the about function just displays the about page and the user can choose to read about NISR or Blue Beatles

def about ():
    user_input = input("You're welcome to the about page, please select an option: \n 1. About NISR \n 2. About Blue Beatles \n 4. Exit \n")
    if user_input == "1":
        paragraph1 = """The National Institute of Statistics of Rwanda (NISR) is a public institution with a legal personality operating under the supervision of the Ministry of Finance and Economic Planning (MINECOFIN).
        It was created by the law n° 04/2013 of 08/02/2013.
        The mission of NISR is to provide relevant, timely and reliable statistical information for evidence-based decision making.
        The vision of NISR is to be a center of excellence in providing statistical information for evidence-based decision making.
        This dashboard in particular fulfils the core mission of NISR as it provides an insight into the labor market in Rwanda
        This dasboard also fulfils the vision of NISR as it provides a platform for the public to access the data and make informed decisions."""
        print(paragraph1)
        input("Press enter to continue")
        about()

    elif user_input == "2":
        paragraph2 = """ Blue Beatles is a team of two aspiring programmers Ken Ganza and Tuyishime Johnson.
        Both Ken and Johnson are students at the African Leadership University pursuing a degree in Software Engineering and they share
        the love of programming and data science. In collaboration with NISR they designed this dashboard to help the public access the data"""
        print(paragraph2)
        input("Press enter to continue")
        about()
    else:
        print("Thank you for visiting the about page")
        input("Press enter to continue")
        return