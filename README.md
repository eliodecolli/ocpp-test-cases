# OCPP 2.0.1 Test Cases

This repository contains test cases for the base implementation of OCPP 2.0.1, based on the official documentation.

## Extraction Process
The script in `main.py` contains the logic used to manually extract text content from the protocol’s PDF.
Editing the script and running it locally allows you to easily generate missing test cases, if needed.

## Test Case Generation
**Each test case is AI-generated.** The agent prompt used to generate the test cases is located in `/.claude/agents/`.

## Coverage
The Transactions, Authorization, and Provision modules have full scenario coverage. The other modules included here contain test cases _only_ for the base implementation of OCPP 2.0.1.

**NOTE**: Several other modules have been completely omitted. You can manually generate additional test cases if needed. Contributions are very welcome.
