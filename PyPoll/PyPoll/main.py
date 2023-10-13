import os
import csv

# Files to upload and output
file_to_load = "resources/election_data.csv"
file_to_output = "analysis/election_analysis_1.txt"

# total vote casted counter
total_votes = 0

#candidate choices and vote counters
candidate_choices = [] 
candidate_votes = {}

#winning candidate and winning count tracking
winning_candidate = ""
winning_count = 0

#read csv and convert it into a dictionary
with open(file_to_load) as election_data:
    csv_reader = csv.DictReader(election_data)

    # loop through row
    for row in csv_reader:

        # Add to total vote count
        total_votes = total_votes + 1

        # Extract the candidate name from each row
        candidate_name = row["Candidate"]

        # if name does not match existing candidate
        if candidate_name not in candidate_choices:

            # Add it to the list of candidates in the running
            candidate_choices.append(candidate_name)

            # Begin counting candidate's vote
            candidate_votes[candidate_name] = 0

            #Add vote to candidate's count
            candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1

# Print results and export data to text file
with open(file_to_output, "w") as txt_file:
     
    # Print final result
    election_results = (
        f"\n\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"-------------------------\n"
    )
    print(election_results)

    #Save final votes to text file
    txt_file.write(election_results)

    # Select winner by looping through the vote counts
    for candidate in candidate_votes:
        
        votes = candidate_votes.get(candidate)
        vote_percentage = float(votes) / float(total_votes)*100

        # Winning vote count and candidate
        if (votes > winning_count):
            winning_count = votes
            winning_candidate = candidate

        # Print each candidate's count and percentage
    voter_output = f"{candidate}: {vote_percentage: .3f}% ({votes})\n"
    print(voter_output)

        # Save it to text file
    txt_file.write(voter_output)

    # Print winning candidate
    winning_candidate_summary = (
        f"-------------------------\n"
        f"winner: {winning_candidate}\n"
        f"-------------------------\n"
    )
    print(winning_candidate_summary)
            