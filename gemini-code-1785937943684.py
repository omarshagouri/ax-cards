# ============================================================
# AGENT 5 · CELL 5 — RUN
# ============================================================

# --- REAL run: refs (visual sheet + output folder) come from the pipeline by video id ---
VIDEO_ID = "AX-TEST-SF"
flagged = await run_agent5(VIDEO_ID)

# --- TEST run against a throwaway sheet/folder (uncomment to use) ---
# flagged = await run_agent5("AX-TEST", sheet_id=TEST_SHEET_ID,
#                             out_folder_id=TEST_OUT_FOLDER, tab="Visual_Plan")