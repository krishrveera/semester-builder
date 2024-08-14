def suggestor():
    # Dictionary to track completion status of university courses
    catalog_2021_all_classes_codes_breakdown = {
        "MAC2281": False,  # Calculus I - viable for AP Calc AB (score of 3 or higher)
        "MAC2311": False,  # Calculus I - viable for AP Calc AB (score of 3 or higher)
        "MAC2282": False,  # Calculus II - viable for AP Calc BC (score of 4 or higher)
        "MAC2312": False,  # Calculus II - viable for AP Calc BC (score of 4 or higher)
        "MAC2283": False,  # Calculus III
        "MAC2313": False,  # Calculus III
        "EGN3000L": False,  # Foundations of Engineering Lab
        "EGN3000": False,  # Foundations of Engineering
        "ENC1101": False,  # Composition I - viable for AP English Lang or AP English Lit (score of 3 or higher)
        "ENC1102": False,  # Composition II - viable for AP English Lang or AP English Lit (score of 4 or higher)
        "PHY2048": False,  # Physics I - viable for AP Physics C: Mech (score of 4 or higher)
        "PHY2048L": False,  # Physics I Lab - viable for AP Physics C: Mech (score of 4 or higher)
        "PHY2049": False,  # Physics II - viable for AP Physics C: EnM (score of 4 or higher)
        "PHY2049L": False,  # Physics II Lab - viable for AP Physics C: EnM (score of 4 or higher)
        "COP2510": False,  # Programming Concepts
        "CDA3103": False,  # Computer Organization
        "COP3514": False,  # Program Design
        "CDA3201L": False,  # Computer Logic Design Lab
        "CDA3201": False,  # Computer Logic Design
        "COP4530": False,  # Data Structures
        "COT3100": False,  # Discrete Structures
        "EGN3443": False,  # Probability and Statistics for Engineers
        "ENG4450": False,  # Linear Systems
        "CDA4205": False,  # Computer Architecture
        "CDA4205L": False,  # Computer Architecture Lab
        "COT4400": False,  # Analysis of Algorithms
        "ENC3246": False,  # Communication for Engineers
        "CNT4419": False,  # Secure Coding
        "COP4600": False,  # Operating Systems
        "CEN4020": False,  # Software Engineering
        "CIS4250": False,  # Ethical Issues and Professional Conduct
        "NSE1": False,  # Natural Science Elective I
        "SSE1": False,  # Social Science Elective
        "HCDE1": False,  # Human and Cultural Diversity Elective
        "NSE2": False,  # Natural Science Elective II
        "CSE1": False,  # CSE Elective
        "CSE2": False,  # CSE Software Elective I
        "CSE3": False,  # CSE Software Elective II
        "CSE4": False,  # CSE Elective I
        "CSE5": False,  # CSE Elective II
        "CSE6": False,  # CSE Elective III
        "CSE7": False,  # CSE Theory Elective
        "GE1": False,  # General Elective I
        "GE2": False,  # General Elective II
        "GE3": False,  # General Elective III
    }

    # Function to update dictionary based on AP scores
    def update_catalog(course_code, ap_score, required_score):
        if ap_score >= required_score:
            catalog_2021_all_classes_codes_breakdown[course_code] = True

    # Get the number of AP exams taken
    num_exams = int(input("How many AP exams have you taken? "))

    for _ in range(num_exams):
        # Validate exam name
        while True:
            exam_name = (
                input("Enter the name of AP exam (e.g. AP Calculus AB): ")
                .strip()
                .lower()
            )
            if exam_name and not exam_name[0].isdigit():
                break
            print("Invalid exam name. The name cannot start with a number.")

        # Validate score input
        while True:
            score_input = input("Enter the score you received: ")
            if score_input.isdigit():
                score = int(score_input)
                break
            print("Invalid score. Please enter an integer.")

        # Update courses based on AP exam and score
        if exam_name in ["ap calc ab", "ap calculus ab"]:
            update_catalog("MAC2281", score, 3)
            update_catalog("MAC2311", score, 3)
        elif exam_name in ["ap calc bc", "ap calculus bc"]:
            update_catalog("MAC2282", score, 4)
            update_catalog("MAC2312", score, 4)
        elif exam_name in [
            "ap english lang",
            "ap english language",
            "ap lang",
            "ap language",
        ]:
            update_catalog("ENC1101", score, 3)
            update_catalog("ENC1102", score, 4)
        elif exam_name in [
            "ap english lit",
            "ap english literature",
            "ap lit",
            "ap literature",
        ]:
            update_catalog("ENC1101", score, 3)
            update_catalog("ENC1102", score, 4)
        elif exam_name in ["ap physics c: mech", "ap physics c: mechanics"]:
            update_catalog("PHY2048", score, 4)
            update_catalog("PHY2048L", score, 4)
        elif exam_name in [
            "ap physics c: enm",
            "ap physics c: electricity and magnetism",
        ]:
            update_catalog("PHY2049", score, 4)
            update_catalog("PHY2049L", score, 4)
        # Add more AP exams and corresponding courses here as needed
        else:
            print("Exam not recognized or no credit available for this course.")

    # Print the percentage of pending courses
    total_courses = len(catalog_2021_all_classes_codes_breakdown)
    completed_courses = sum(
        completed for completed in catalog_2021_all_classes_codes_breakdown.values()
    )
    pending_courses = total_courses - completed_courses
    pending_percentage = (pending_courses / total_courses) * 100
    print(f"\nPercentage of courses still pending: {pending_percentage:.2f}%")


# Call the function to start the CLI
suggestor()
