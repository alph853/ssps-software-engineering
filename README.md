# Student Smart Printing Service (HCMUT_SSPS)

## Overview
The **Student Smart Printing Service (HCMUT_SSPS)** is a system designed to streamline document printing for students across the university campuses. This service allows students to upload documents, select printers, and customize printing preferences, while ensuring efficient management and logging of printing activities.

---

## Key Features

### For Students:
- **Document Printing**:
  - Upload document files to the system.
  - Select a printer and configure printing properties (e.g., paper size, page range, single/double-sided, number of copies).
  - Supported file types are configured by the **Student Printing Service Officer (SPSO)**.
  
- **Printing Logs**:
  - View personal printing history for a specific time period.
  - Access a summary of printed pages categorized by page size.

- **Account Management**:
  - Default semester quota for A4-size pages.
  - Option to purchase additional pages using the **Buy Printing Pages** feature.
  - Online payment integration with the university's BKPay system.
  - Printing is restricted by the available page balance (e.g., 1 A3 page = 2 A4 pages).

### For Student Printing Service Officer (SPSO):
- **Printer Management**:
  - Add, enable, or disable printers.
  - Maintain printer details such as ID, brand, model, description, and location (campus, building, room).

- **System Configuration**:
  - Manage default printing quotas and distribution dates.
  - Set permitted file types for document uploads.

- **Printing History and Reports**:
  - View detailed printing logs of all students or specific students for a given time period and printer(s).
  - Access monthly and yearly usage reports, automatically generated and stored within the system.

### Security:
- All users are authenticated via the **HCMUT_SSO authentication service** before accessing the system.

---

## System Overview

### Printer Details:
Each printer is registered with the system, containing the following attributes:
- Printer ID
- Brand/Manufacturer
- Model
- Description
- Location (Campus, Building, Room)

### Printing Logs:
Logs capture critical details, including:
- Student ID and Printer ID
- File name
- Printing start and end times
- Pages printed (by size) and number of copies

### Page Quota and Balances:
- Each student is allocated a default number of A4-size pages per semester.
- Additional pages can be purchased, and quotas are managed accordingly.
- System prevents overprinting by ensuring the balance is sufficient.

---

## Folder Structure
- **Reports**: Contains project reports, including the [Final Report](Report/Report.pdf) and any supplementary documentation.

---

## How to Use
### For Students:
1. Log in using your university credentials via the HCMUT_SSO authentication service.
2. Upload your document and configure printing settings.
3. Select a printer and submit your printing request.

### For SPSO:
1. Access the administrative portal to manage printers and system configurations.
2. Generate and view reports or analyze printing logs as needed.

---

## Contributors

| Name    			| Student ID|
| ----------------- | ------- 	|
| Do Quang Khanh	| 2053106   |
| Ho Minh Hoang  	| 2211073   |
| Do Thanh Trung    | 2252853   |
| Ha The Binh 		| 2152435	|
| Hoang Huy Minh	| 2053212	|


---

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

