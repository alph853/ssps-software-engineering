from base.models import Student, Printer
import random

students: list[Student] = [
    Student(
        student_id="2252001",
        fname="An",
        lname="Nguyen Van",
        email="an.nguyen@hcmut.edu.vn",
        page_balance=200
    ),
    Student(
        student_id="2252002",
        fname="Binh",
        lname="Tran Thi",
        email="binh.tran@hcmut.edu.vn",
        page_balance=200
    ),
    Student(
        student_id="2252003",
        fname="Chien",
        lname="Le Van",
        email="chien.le@hcmut.edu.vn",
        page_balance=200
    ),
    Student(
        student_id="2252004",
        fname="Dung",
        lname="Pham Thi",
        email="dung.thi@hcmut.edu.vn",
        page_balance=200
    ),
    Student(
        student_id="2252005",
        fname="Hoa",
        lname="Nguyen Thi",
        email="hoa.nguyen@hcmut.edu.vn",
        page_balance=200
    ),
    Student(
        student_id="2252006",
        fname="Long",
        lname="Pham Van",
        email="long.pham@hcmut.edu.vn",
        page_balance=200
    ),
    Student(
        student_id="2252007",
        fname="Minh",
        lname="Le Thi",
        email="minh.le@hcmut.edu.vn",
        page_balance=200
    ),
    Student(
        student_id="2252008",
        fname="Trang",
        lname="Tran Thi",
        email="trang.tran@hcmut.edu.vn",
        page_balance=200
    ),
    Student(
        student_id="2252009",
        fname="Thang",
        lname="Hoang Van",
        email="thang.hoang@hcmut.edu.vn",
        page_balance=200
    ),
    Student(
        student_id="2252010",
        fname="Anh",
        lname="Vu",
        email="anh.vu@hcmut.edu.vn",
        page_balance=200
    ),
    Student(
        student_id="2252011",
        fname="Huong",
        lname="Bui Thi",
        email="huong.bui@hcmut.edu.vn",
        page_balance=200
    ),
    Student(
        student_id="2252012",
        fname="Lan",
        lname="Do",
        email="lan.do@hcmut.edu.vn",
        page_balance=200
    ),
    Student(
        student_id="2252013",
        fname="Quang",
        lname="Pham",
        email="quang.pham@hcmut.edu.vn",
        page_balance=200
    ),
    Student(
        student_id="2252014",
        fname="Tu",
        lname="Tran",
        email="tu.tran@hcmut.edu.vn",
        page_balance=200
    ),
]

students.extend([
    Student(
        student_id="2252015",
        fname="Bao",
        lname="Nguyen Van",
        email="bao.nguyen@hcmut.edu.vn",
        page_balance=200
    ),
    Student(
        student_id="2252016",
        fname="Cuong",
        lname="Tran Dinh Manh",
        email="cuong.tran@hcmut.edu.vn",
        page_balance=200
    ),
    Student(
        student_id="2252017",
        fname="Dai",
        lname="Le Vinh",
        email="dai.le@hcmut.edu.vn",
        page_balance=200
    ),
    Student(
        student_id="2252018",
        fname="Giang",
        lname="Pham Thi Huong",
        email="giang.pham@hcmut.edu.vn",
        page_balance=200
    ),
    Student(
        student_id="2252019",
        fname="Hieu",
        lname="Hoang Van Ngoc",
        email="hieu.hoang@hcmut.edu.vn",
        page_balance=200
    ),
    Student(
        student_id="2252020",
        fname="Khanh",
        lname="Vu Minh",
        email="khanh.vu@hcmut.edu.vn",
        page_balance=200
    ),
    Student(
        student_id="2252021",
        fname="Linh",
        lname="Bui Lan Phuong",
        email="linh.bui@hcmut.edu.vn",
        page_balance=200
    ),
    Student(
        student_id="2252022",
        fname="Mai",
        lname="Do Quang",
        email="mai.do@hcmut.edu.vn",
        page_balance=200
    ),
    Student(
        student_id="2252023",
        fname="Nam",
        lname="Nguyen Trinh Tran",
        email="nam.nguyen@hcmut.edu.vn",
        page_balance=200
    ),
    Student(
        student_id="2252024",
        fname="Phuc",
        lname="Tran Le Tien",
        email="phuc.tran@hcmut.edu.vn",
        page_balance=200
    ),
    Student(
        student_id="2252025",
        fname="Quyen",
        lname="Le Song",
        email="quyen.le@hcmut.edu.vn",
        page_balance=200
    ),
    Student(
        student_id="2252026",
        fname="Son",
        lname="Pham Truc",
        email="son.pham@hcmut.edu.vn",
        page_balance=200
    ),
    Student(
        student_id="2252027",
        fname="Tam",
        lname="Hoang Manh",
        email="tam.hoang@hcmut.edu.vn",
        page_balance=200
    ),
    Student(
        student_id="2252028",
        fname="Uyen",
        lname="Vu Thi To",
        email="uyen.vu@hcmut.edu.vn",
        page_balance=200
    ),
    Student(
        student_id="2252029",
        fname="Vinh",
        lname="Bui Vuong",
        email="vinh.bui@hcmut.edu.vn",
        page_balance=200
    ),
    Student(
        student_id="2252030",
        fname="Yen",
        lname="Do Kim",
        email="yen.do@hcmut.edu.vn",
        page_balance=200
    ),
    Student(
        student_id="2252031",
        fname="An",
        lname="Nguyen",
        email="an.nguyen2@hcmut.edu.vn",
        page_balance=200
    ),
    Student(
        student_id="2252032",
        fname="Binh",
        lname="Tran",
        email="binh.tran2@hcmut.edu.vn",
        page_balance=200
    ),
    Student(
        student_id="2252033",
        fname="Chien",
        lname="Le Ngoc Minh",
        email="chien.le2@hcmut.edu.vn",
        page_balance=200
    ),
    Student(
        student_id="2252034",
        fname="Anh",
        lname="Ha Minh",
        email="dung.pham2@hcmut.edu.vn",
        page_balance=200
    ),
])


class PrinterStatus:
    ENABLED = 'Đang hoạt động'
    DISABLED = 'Vô hiệu hóa'
    MALFUNCTIONED = 'Gặp sự cố'
    FULL = 'Hàng đợi đầy'


printers = [
    Printer(
        brand="HP",
        model="LaserJet Pro M404",
        description="High-speed black and white laser printer.",
        building="B1",
        room="101",
        status=PrinterStatus.ENABLED,
        total_pages_used=15000,
        campus='Lý Thường Kiệt'
    ),
    Printer(
        brand="Canon",
        model="Pixma TS9120",
        description="Wireless all-in-one photo printer.",
        building="C6",
        room="202",
        status=PrinterStatus.ENABLED,
        total_pages_used=8000,
        campus='Lý Thường Kiệt'
    ),
    Printer(
        brand="Brother",
        model="HL-L2350DW",
        description="Compact monochrome laser printer.",
        building="B2",
        room="103",
        status=PrinterStatus.FULL,
        total_pages_used=20000,
        campus='Lý Thường Kiệt'
    ),
    Printer(
        brand="Epson",
        model="EcoTank ET-4760",
        description="All-in-one inkjet with refillable tanks.",
        building="B4",
        room="305",
        status=PrinterStatus.DISABLED,
        total_pages_used=5000,
        campus='Lý Thường Kiệt'
    ),
    Printer(
        brand="Samsung",
        model="Xpress M2020W",
        description="Wireless monochrome laser printer.",
        building="C4",
        room="204",
        status=PrinterStatus.MALFUNCTIONED,
        total_pages_used=12000,
        campus='Lý Thường Kiệt'
    ),
    Printer(
        brand="HP",
        model="DeskJet 3755",
        description="Compact all-in-one printer.",
        building="B4",
        room="401",
        status=PrinterStatus.ENABLED,
        total_pages_used=3000,
        campus='Lý Thường Kiệt'
    ),
    Printer(
        brand="Canon",
        model="ImageCLASS LBP6230dw",
        description="Wireless monochrome laser printer.",
        building="B1",
        room="104",
        status=PrinterStatus.ENABLED,
        total_pages_used=18000,
        campus='Lý Thường Kiệt'
    ),
    Printer(
        brand="Brother",
        model="MFC-J805DW",
        description="Inkjet all-in-one with high page yield.",
        building="B4",
        room="306",
        status=PrinterStatus.ENABLED,
        total_pages_used=7000,
        campus='Lý Thường Kiệt'
    ),
    Printer(
        brand="Epson",
        model="WorkForce WF-2830",
        description="All-in-one wireless color inkjet.",
        building="B11",
        room="402",
        status=PrinterStatus.FULL,
        total_pages_used=9000,
        campus='Lý Thường Kiệt'
    ),
    Printer(
        brand="Samsung",
        model="ProXpress SL-M2020",
        description="Compact monochrome laser printer.",
        building="C2",
        room="205",
        status=PrinterStatus.ENABLED,
        total_pages_used=16000,
        campus='Lý Thường Kiệt'
    ),
    Printer(
        brand="HP",
        model="OfficeJet Pro 9015",
        description="All-in-one wireless color printer.",
        building="H1",
        room="307",
        status=PrinterStatus.DISABLED,
        total_pages_used=11000,
        campus='Dĩ An'
    ),
    Printer(
        brand="Canon",
        model="Pixma TR8520",
        description="All-in-one wireless printer with scanner.",
        building="B12",
        room="403",
        status=PrinterStatus.ENABLED,
        total_pages_used=4000,
        campus='Lý Thường Kiệt'
    ),
    Printer(
        brand="Brother",
        model="HL-L2395DW",
        description="Wireless monochrome laser printer with scanner.",
        building="H1",
        room="105",
        status=PrinterStatus.ENABLED,
        total_pages_used=14000,
        campus='Dĩ An'
    ),
    Printer(
        brand="Epson",
        model="Expression Home XP-4100",
        description="Compact wireless color printer.",
        building="H2",
        room="206",
        status=PrinterStatus.FULL,
        total_pages_used=6000,
        campus='Dĩ An'
    ),
    Printer(
        brand="Samsung",
        model="Xpress C1810W",
        description="Color laser printer with wireless connectivity.",
        building="B4",
        room="308",
        status=PrinterStatus.ENABLED,
        total_pages_used=13000,
        campus='Lý Thường Kiệt'
    ),
    Printer(
        brand="HP",
        model="LaserJet Pro M15w",
        description="Compact wireless monochrome laser printer.",
        building="B6",
        room="404",
        status=PrinterStatus.ENABLED,
        total_pages_used=2500,
        campus='Lý Thường Kiệt'
    ),
    Printer(
        brand="Canon",
        model="Maxify MB5420",
        description="High-volume color inkjet printer.",
        building="H2",
        room="106",
        status=PrinterStatus.MALFUNCTIONED,
        total_pages_used=22000,
        campus='Dĩ An'
    ),
    Printer(
        brand="Brother",
        model="DCP-L2550DW",
        description="Monochrome laser all-in-one printer.",
        building="H6",
        room="207",
        status=PrinterStatus.ENABLED,
        total_pages_used=17500,
        campus='Dĩ An'
    ),
    Printer(
        brand="Epson",
        model="WorkForce Pro WF-4740",
        description="All-in-one wireless color inkjet.",
        building="B4",
        room="309",
        status=PrinterStatus.DISABLED,
        total_pages_used=8500,
        campus='Lý Thường Kiệt'
    ),
    Printer(
        brand="Samsung",
        model="SL-M2875FD",
        description="Color laser all-in-one printer.",
        building="B9",
        room="405",
        status=PrinterStatus.DISABLED,
        total_pages_used=9500,
        campus='Lý Thường Kiệt'
    ),
]

document_names = [
    "Annual_Report_2023.pdf",
    "Project_Plan_Q1.docx",
    "meeting_minutes_march.pdf",
    "Financial_Statement_April.xlsx",
    "marketing_strategy_presentation.pptx",
    "Employee_Handbook.pdf",
    "Research_Paper_Final.docx",
    "Client_Proposal_V1.pdf",
    "sales_data_january.xlsx",
    "technical_specs_v2.pdf",
    "Budget_Overview_2023.xlsx",
    "design_sketches_april.png",
    "User_Guide.pdf",
    "Product_Catalog.docx",
    "invoice_10234.pdf",
    "press_release_may.pdf",
    "Training_Materials.pptx",
    "Contract_Agreement_2023.pdf",
    "inventory_list_june.xlsx",
    "Company_Policy.pdf",
    "event_plan_summer.docx",
    "Software_Architecture_Diagram.eps",
    "Employee_Performance_Review_2023.pdf",
    "customer_feedback_survey.xlsx",
    "Newsletter_March_2023.pdf",
    "quality_assurance_report.pdf",
    "Procurement_List_July.xlsx",
    "Safety_Protocols.pdf",
    "strategic_partnership_agreement.docx",
    "Marketing_Campaign_Data_July.xlsx",
    "Board_Meeting_Agenda.pdf",
    "product_launch_presentation.pptx",
    "IT_Security_Policy.pdf",
    "Vendor_Contracts_2023.pdf",
    "Research_Proposal_V3.docx",
    "Budget_Allocation_July.xlsx",
    "technical_manual.pdf",
    "social_media_strategy.pptx",
    "Product_Feature_List.pdf",
    "Customer_Support_Guide.docx",
    "HR_Onboarding_Process.pdf",
    "sales_pipeline_july.xlsx",
    "Website_Content_Update.docx",
    "data_analysis_report_july.pdf",
    "Marketing_Materials_September.pptx",
    "Project_Timeline_2023.xlsx",
    "budget_reconciliation_june.pdf",
    "employee_exit_form.docx",
    "Technical_Briefing.pdf",
    "Market_Research_Data_July.xlsx",
    "Product_Backlog_July.docx",
    "Annual_Summary_Report.pdf",
    "Project_Update_September.pptx",
    "Employee_Survey_2023.xlsx",
    "sales_report_july.pdf",
    "Product_Requirements.docx",
    "Vendor_Evaluation_Report.pdf",
    "marketing_strategy_update.pptx",
    "customer_onboarding_guide.pdf",
    "Financial_Planning_July.xlsx",
    "product_testing_results.pdf",
    "Employee_Training_Records.docx",
    "Project_Brief.pdf",
    "sales_strategy_july.pptx",
    "Marketing_Data_Analysis.xlsx",
    "product_feedback_survey.pdf",
    "Company_Annual_Presentation.pptx",
    "Client_Contracts_July.docx",
    "Financial_Report_Q2_2023.pdf",
    "Project_Presentation_August.pptx",
    "Marketing_Budget_July.xlsx",
    "Employee_Benefits_Guide.pdf",
    "Sales_Targets_July.xlsx",
    "product_lifecycle_overview.pdf",
    "HR_Policies_and_Procedures.docx",
    "market_trend_analysis.pdf",
    "Project_Closure_Report.pdf",
    "customer_retention_strategy.pptx",
    "Financial_Audit_July.xlsx",
    "Product_Development_Roadmap.pdf",
    "Marketing_Campaign_Strategy.docx",
    "Employee_Handbook_2023.pdf",
    "sales_pipeline_update.pptx",
    "Product_Performance_Metrics.xlsx",
    "Company_Mission_and_Vision.pdf",
    "market_expansion_plan.docx",
    "Project_Risk_Assessment.pdf",
    "Customer_Engagement_Report.pptx",
    "Financial_Projection_2023.xlsx",
    "product_innovation_presentation.pdf",
    "Marketing_Social_Media_Plan.pptx",
    "Employee_Recognition_Program.pdf",
    "sales_forecast_july.xlsx",
    "Product_Strategy_Document.docx",
    "Company_Annual_Report_2023.pdf",
    "market_survey_results.pptx",
    "Project_Implementation_Plan.xlsx",
    "team_meeting_notes_august.docx",
    "expense_report_july.xlsx",
    "product_update_v1.pdf",
    "customer_support_ticket_12345.pdf",
    "annual_financial_summary.pdf",
    "marketing_campaign_q3.pptx",
    "employee_schedule_september.xlsx",
    "training_video_part1.mp4",
    "safety_inspection_report.pdf",
    "client_feedback_form.docx",
    "logistics_plan_september.xlsx",
    "research_data_analysis.pdf",
    "strategic_planning_meeting.pptx",
    "it_support_guidelines.pdf",
    "budget_request_form.docx",
    "new_hire_orientation_schedule.pdf",
    "product_catalog_update_september.docx",
    "customer_satisfaction_survey_results.xlsx",
    "project_status_report_september.pdf",
    "web_analytics_report_july.pdf",
    "event_invitation_list.xlsx",
    "vendor_contract_review.docx",
    "social_media_content_calendar.xlsx",
    "branding_guidelines.pdf",
    "staff_vacation_schedule.xlsx",
    "project_requirements_document.docx",
    "market_competitor_analysis.pdf",
    "financial_risk_assessment.xlsx",
    "employee_feedback_summary.pdf",
    "product_warranty_information.docx",
    "training_material_update.pptx",
    "customer_loyalty_program.pdf",
    "sales_performance_review.xlsx",
    "company_organization_chart.vsdx",
    "quality_control_procedures.pdf",
    "marketing_collateral_request_form.docx",
    "inventory_restocking_schedule.xlsx",
    "software_update_log.txt",
    "client_presentation_september.pptx",
    "project_milestones_timeline.xlsx",
    "employee_contact_list.xlsx",
    "seo_report_august.pdf",
    "product_user_manual.pdf",
    "customer_service_protocol.docx",
    "financial_statement_q3.pdf",
    "event_sponsorship_proposal.docx",
    "training_schedule_october.xlsx",
    "strategic_initiatives_overview.pdf",
    "it_asset_inventory.xlsx",
    "employee_engagement_survey_results.pdf",
    "security_policy_update.docx",
    "budget_forecast_2024.xlsx",
    "product_release_notes.pdf",
    "marketing_performance_dashboard.xlsx",
    "supplier_evaluation_form.docx",
    "conference_agenda.pdf",
    "project_deliverables_list.xlsx",
    "employee_benefits_enrollment_form.docx",
    "customer_relationship_management_plan.pdf",
    "sales_kpi_overview.xlsx",
    "company_announcements_september.docx",
    "brand_awareness_study.pdf",
    "project_budget_adjustment_request.xlsx",
    "employee_training_feedback_form.docx",
    "product_return_policy.pdf",
    "meeting_schedule_october.xlsx",
    "market_segmentation_analysis.pdf",
    "financial_compliance_report.docx",
    "team_building_activity_plan.pdf",
    "vendor_purchase_order_12345.xlsx",
    "customer_account_overview.pdf",
    "product_design_specifications.docx",
    "marketing_email_templates.pptx",
    "hr_policy_update_september.pdf",
    "sales_incentive_program.pdf",
    "project_charter_document.docx",
    "customer_success_story_september.pdf",
    "expense_policy_guidelines.docx",
    "it_system_maintenance_schedule.xlsx",
    "webinar_presentation_materials.pptx",
    "product_training_manual.pdf",
    "market_penetration_strategy.docx",
    "financial_review_meeting_minutes.pdf",
    "employee_performance_metrics.xlsx",
    "product_demo_schedule.docx",
    "marketing_trends_analysis.pdf",
    "security_audit_report.pdf",
    "project_transition_plan.xlsx",
    "customer_acquisition_cost_analysis.docx",
    "employee_wellness_program.pdf",
    "budget_variance_report_september.xlsx",
    "product_feature_specification.pdf",
    "social_media_engagement_report.xlsx",
    "customer_retention_metrics.docx",
    "company_culture_deck.pptx",
    "quality_assurance_checklist.pdf",
    "employee_exit_interview_form.docx",
    "market_opportunity_assessment.pdf",
    "financial_planning_strategy.docx",
    "project_lesson_learned_document.pdf",
    "customer_service_training_materials.pptx",
    "sales_call_report_form.docx",
    "marketing_automation_workflow.docx",
]