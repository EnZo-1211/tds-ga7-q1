from fastapi import APIRouter, Request
import re

router = APIRouter()

@router.post("/release-gate")
async def release_gate(request: Request):
    data = await request.json()
    violations = []
    
    workflow = data.get("workflow", {})
    image = data.get("image", {})

    # 1. EXCESS_PERMISSION
    allowed_perms = {"contents": "read", "packages": "write", "id-token": "none"}
    if workflow.get("permissions") != allowed_perms:
        violations.append("EXCESS_PERMISSION")

    # 2. UNSAFE_PR_TRIGGER
    if data.get("event") == "pull_request":
        if workflow.get("trigger") != "pull_request":
            violations.append("UNSAFE_PR_TRIGGER")

    # 3. TESTS_INCOMPLETE
    if not (workflow.get("testsPassed") is True and workflow.get("matrixComplete") is True and workflow.get("failFast") is False):
        violations.append("TESTS_INCOMPLETE")

    # 4. MUTABLE_ACTION
    actions = workflow.get("actions", [])
    for action in actions:
        if action.get("owner") != "actions":
            ref = action.get("ref", "")
            if not re.match(r"^[0-9a-f]{40}$", ref):
                violations.append("MUTABLE_ACTION")
                break

    # 5. SINGLE_STAGE_IMAGE
    if image.get("multiStage") is not True:
        violations.append("SINGLE_STAGE_IMAGE")

    # 6. ROOT_RUNTIME
    if image.get("runsAsRoot") is not False:
        violations.append("ROOT_RUNTIME")

    # 7. SECRET_IN_LAYER
    if image.get("secretMode") not in ("none", "buildkit"):
        violations.append("SECRET_IN_LAYER")

    # 8. CRITICAL_CVE
    if image.get("criticalVulnerabilities") != 0:
        violations.append("CRITICAL_CVE")

    # 9. UNPINNED_IMAGE
    if image.get("digestPinned") is not True:
        violations.append("UNPINNED_IMAGE")

    # 10. INVALID_PRODUCTION_REF & APPROVAL_REQUIRED
    if data.get("target") == "production":
        if data.get("event") != "push" or data.get("ref") != "refs/heads/main":
            violations.append("INVALID_PRODUCTION_REF")
        if workflow.get("environmentApproval") is not True:
            violations.append("APPROVAL_REQUIRED")

    decision = "promote" if not violations else "block"
    
    return {
        "decision": decision,
        "violations": violations
    }
