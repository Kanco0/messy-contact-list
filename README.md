<p align="center"><b>2026-01-20</b></p>
<h1 align="center">📊 Dataset:Contact List</h1>

<h2 align="center">📌 Project Summary:<br> Contact List Cleanup</h2>

The Problem:
The contact list was very messy and unreliable. Phone numbers were written in different ways, some emails were invalid or missing, names were inconsistent, and many people appeared more than once. In this state, the data could not be used safely for contacting customers or making decisions.

What I Did:
I focused on making the data usable instead of trying to “guess” or fix broken information. I standardized phone numbers into one clear format, cleaned names so they looked consistent, checked that emails followed a valid structure, and removed duplicate entries. Records that could not be trusted were filtered out rather than forced to fit.

The Result:
After cleaning and validating the records, only contacts with complete and usable information were kept. The dataset was reduced from about 1,000 rows to 31 reliable contacts. While much smaller, every remaining entry is accurate, consistent, and ready for real-world use. This project prioritizes data quality over quantity and reflects realistic data cleaning decisions.

📁 Repository contains:
raw_data/ → Original CSV files
cleaned_data/ → Final merged and cleaned dataset
scripts/ → Python scripts for cleaning

<hr>
<h3>🫧 The Cleaning Procces:</h3>
ok first thing after using <code>print(df)</code>
is to clean numbers to the same identical number format using regex. it deletes everything that isn’t a number, such as spaces or symbols, and then creates a new column which is named <code>Clean_Phone</code>. it has the correct unified format and only numbers that are 10 or 11 characters long. checking the <code>Clean_Phone</code> column is important because it’s cleaned, unified, and has no spaces or symbols. this will be good for sending texts or contacting in the future.

in the names, I used <code>.strip()</code> and made the first letter uppercase using <code>.title()</code>.

making sure the email format is right by also using regex to check for a basic email structure.

then deleting the duplication based on the name and email. deleting based on only one column isn’t right because people can have identical names.

lastly, I kept only the rows that have a valid email and a valid number,
and deleted the <code>Email_Valid</code> column since I don’t need it anymore,
then saved the file at the end.

after a day, I went back and checked how many rows were there and how many I deleted. it turned out that from around 1k rows, all I got is 31. this is because I prioritize data usability over data retention. records that have wrong or unusable information were deleted.
