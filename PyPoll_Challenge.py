# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize variables
total_votes = 0 
#candidate
candidate_options = []
candidate_votes = {}
#county
county_options = []
county_dict = {}
#winning candidate
winning_candidate = ""
winning_count = 0
winning_percentage = 0
#winning county
winning_county = ""
highest_count_county = 0
highest_percentage_county = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    # Read and print the header row.
    headers = next(file_reader)
    for row in file_reader:
        total_votes += 1
        candidate_name = row[2]

        county_name = row[1]

        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1

 # count counties in rows
        
        if county_name not in county_options:
            county_options.append(county_name)
            county_dict[county_name] = 0
        
        county_dict[county_name] += 1

with open(file_to_save, "w") as txt_file: 
        # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")  
    txt_file.write(election_results)   
       
    # for county loop with county list
    county_sum1 = (f"\nCounty Votes:\n")
    print(county_sum1)  
   
    for county in county_dict:
        votes = county_dict[county]
        vote_percentage = int(votes) / int(total_votes) * 100
        county_results = (
            f"{county}: {vote_percentage:.1f}% ({votes:,})\n")
        print(county_results)
        txt_file.write(county_results)
        if (votes > highest_count_county) and (vote_percentage > highest_percentage_county):
            highest_count_county = votes
            highest_percentage_county = vote_percentage

            highest_turnout_county = county

        winning_county_summary = (
        f"-------------------------\n"
        f"Largest County Turnout: {highest_turnout_county}\n"
        f"-------------------------\n")
   
    txt_file.write(winning_county_summary)
    print(winning_county_summary)

    for candidate in candidate_votes:
        votes = candidate_votes[candidate]
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
        f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
        txt_file.write(candidate_results)
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)



    





