import re

# Step 1: Take file name from user
filename = input("Enter file name (with extension): ")

try:
    # Step 2: Read file
    with open(filename, "r") as file:
        content = file.read()

    # Step 3: Extract all emails using regex
    all_emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]+', content)

    # Step 4: Remove duplicates
    all_emails = list(set(all_emails))

    # Step 5: Sort alphabetically
    all_emails.sort()

    # Step 6: Extract Gmail addresses
    gmail_emails = [email for email in all_emails if email.endswith("@gmail.com")]


    # Step 7: Ask for Output file name
    output_filename = input("Enter output file name (default: output): ")
    if not output_filename:
        output_filename = "output.txt"
    else:
        if not output_filename.endswith(".txt"):
            output_filename += ".txt"

    # Step 8: Write results to output file
    with open(output_filename, "w") as out:
        
        # Write All Emails Section
        out.write("===== ALL EMAILS =====\n")
        out.write(f"Total Emails: {len(all_emails)}\n\n")
        
        for i, email in enumerate(all_emails, start=1):
            out.write(f"{i}. {email}\n")

        # Write Gmail Section
        out.write("\n===== GMAIL ADDRESSES =====\n")
        out.write(f"Total Gmail Addresses: {len(gmail_emails)}\n\n")
        
        for i, email in enumerate(gmail_emails, start=1):
            out.write(f"{i}. {email}\n")

    # Step 9: Print summary
    print("\nTask Completed Successfully ✅")
    print(f"Total Emails Found: {len(all_emails)}")
    print(f"Gmail Addresses Found: {len(gmail_emails)}")
    print(f"Results saved in {output_filename}")

except FileNotFoundError:
    print("Error: File not found!")




input("Press Enter to exit...")