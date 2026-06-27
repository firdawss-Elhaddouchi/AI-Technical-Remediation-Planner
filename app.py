import json
import streamlit as st

from core.matrix_calculator import (
    load_audit_report,
    calculate_priority_metrics
)

from core.llm_client import generate_remediation_plan

import pandas as pd

# -------------------------------------------------
# Streamlit Page Configuration
# -------------------------------------------------

st.set_page_config(
    page_title="AI Technical Remediation Platform",
    layout="wide"
)

st.title("🛠️ AI Technical Remediation & Backlog Generator")
st.subheader(
    "Transformez un rapport d'audit technique en plan de remédiation et backlog Agile."
)

# -------------------------------------------------
# Load Audit Report
# -------------------------------------------------

uploaded_file = st.file_uploader(
    "📂 Upload Audit Report (JSON)",
    type=["json"]
)

if uploaded_file is None:
    st.info("Please upload an audit report to continue.")
    st.stop()

raw_data = json.load(uploaded_file)

st.success(f"Loaded file: {uploaded_file.name}")

processed_findings = calculate_priority_metrics(
    raw_data["findings"]
)

# -------------------------------------------------
# Project Overview
# -------------------------------------------------

col1, col2, col3 = st.columns(3)

col1.metric(
    "Total Findings",
    len(processed_findings)
)

col2.metric(
    "Framework",
    raw_data["audit_metadata"]["repository"]["framework"]
)

col3.metric(
    "Initial Test Coverage",
    f"{raw_data['audit_metadata']['repository']['coverage']}%"
)

st.divider()

# -------------------------------------------------
# AI Processing
# -------------------------------------------------

if st.button("🚀 Generate Remediation Plan"):

    with st.spinner("The AI is analyzing the audit findings..."):

        try:

            ai_output = generate_remediation_plan(
                processed_findings
            )

            remediations_dict = {
                item["id"]: item
                for item in ai_output["remediations"]
            }

            st.success(
                "The remediation plan has been generated successfully."
            )

            backlog_data = []
            total_effort = 0

            for finding in processed_findings:

                ai_data = remediations_dict.get(
                    finding["id"],
                    {}
                )

                estimated_days = ai_data.get(
                    "estimated_days",
                    0
                )

                total_effort += estimated_days

                backlog_data.append({

                "ID": finding["id"],

                "Domain": finding["domain"],

                "Issue Type": finding["issue_type"],

                "Priority Score": finding["priority_metrics"]["priority_score"],

                "Estimated (Days)": estimated_days,

                "Status": "To Do",

                "Dependencies":
                    ", ".join(
                        ai_data.get("dependencies", [])
                    ) if ai_data.get("dependencies")
                    else "None",

                "Remediation":
                    ai_data.get("remediation", ""),

                "User Story":
                    ai_data.get("user_story", "")

            })

            st.info(
                f"📊 Total Estimated Effort : {total_effort} Man-Days"
            )

            st.dataframe(
                backlog_data,
                use_container_width=True
            )

            df = pd.DataFrame(backlog_data)

            csv = df.to_csv(
                index=False
            ).encode("utf-8")

            st.download_button(
                label="📥 Download Backlog (CSV)",
                data=csv,
                file_name="technical_backlog.csv",
                mime="text/csv"
            )

            st.divider()

            st.header(
                "📋 Agile Tasks Details"
            )

            for task in backlog_data:

                with st.expander(
                    f"{task['ID']} - {task['Issue Type']}"
                ):

                    st.write(
                        f"**Priority Score :** {task['Priority Score']}"
                    )

                    st.write(
                        f"**Estimated Effort :** {task['Estimated (Days)']} day(s)"
                    )

                    st.write(
                        f"**Dependencies :** {task['Dependencies']}"
                    )

                    st.write(
                        "**User Story**"
                    )

                    st.write(
                        task["User Story"]
                    )

                    st.write(
                        "**Technical Remediation**"
                    )

                    st.write(
                        task["Remediation"]
                    )

                    criteria = remediations_dict.get(
                        task["ID"],
                        {}
                    ).get(
                        "acceptance_criteria",
                        []
                    )

                    st.write(
                        "**Acceptance Criteria**"
                    )

                    if criteria:

                        for item in criteria:
                            st.write(
                                f"• {item}"
                            )

                    else:

                        st.write(
                            "No acceptance criteria generated."
                        )

        except Exception as e:

            st.error(
                f"An error occurred while generating the remediation plan:\n\n{e}"
            )