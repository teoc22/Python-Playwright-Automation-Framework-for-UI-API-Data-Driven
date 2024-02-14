# Description

This Python Accelerator Project is designed to streamline the testing of the applications, focusing on UI and API testing frameworks. Utilizing Playwright for end-to-end browser testing and pytest for organizing tests, this project provides a solid foundation for testing robust Python applications. By incorporating Data Driven Testing (DDT) methodologies, it allows for a more dynamic and comprehensive testing approach, significantly improving test coverage and reliability.

## Project Structure

The project highlevel structure looks like this:

- `Engine/`: Contains core functionality including the UI and browser interactions (`Browser/`), Page Object Models (`POM/`) and API Wrappers (`API/`)
- `Playground/Tests/`: Houses all test scripts, separated into API and UI tests for easy management and execution.
- `Resources/`: Includes utility files like `UI/` configurations and `API/` endpoints.

The project detailed structure looks like this:

Project_Root/
│
├── .gitignore
├── logger_config.py
├── pytest.ini
│
├── Engine/
│   ├── API/
│   │   └── api_wrappers.py
│   │
│   └── UI/
│       ├── Browser/
│       │   ├── browser_actions.py
│       │   └── browser_setup.py
│       │
│       └── POM/
│           ├── analyse_statistics_page.py
│           ├── base_page.py
│           ├── configure_synthetic_data_page.py
│           ├── generate_synthetic_data_page.py
│           ├── save_export_project_page.py
│           └── upload_data_page.py
│
├── Playground/
│   └── Tests/
│       ├── API/
│       │   ├── test_api_delete_request.py
│       │   ├── test_api_get_request.py
│       │   ├── test_api_post_request.py
│       │   └── test_api_put_request.py
│       │
│       └── UI/
│           ├── test_data_driven.py
│           ├── test_end_to_end.py
│           ├── test_navigation_error_handling.py
│           ├── test_navigation_from_data_generation_to_save_project.py
│           ├── test_navigation_to_analyze_statistics_page.py
│           ├── test_navigation_to_configure_synthetic_data_page.py
│           └── test_navigation_to_upload_data_page.py
│
└── Resources/
├── API/
│   ├── endpoints_api.py
│   ├── file_path_api.py
│   └── project_name_api.py
│
└── UI/
├── file_path_ui.py
├── initial_url_ui.py
├── project_name_ui.py
└── test_data.py
