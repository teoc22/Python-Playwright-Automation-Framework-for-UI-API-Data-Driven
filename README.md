# Description

This Python Accelerator Project is designed to streamline the testing of the application, focusing on UI and API testing frameworks. Utilizing Playwright for end-to-end browser testing and pytest for organizing tests, this project provides a solid foundation for testing robust Python application. By incorporating Data Driven Testing (DDT) methodology, it allows for a more dynamic and comprehensive testing approach, significantly improving test coverage and reliability.

## Project Structure
```
The project highlevel structure looks like this:

1.Engine/: Core of the automation framework, handling direct interactions with the application under test. It's divided into two main parts:

a). UI/: Contains tools and utilities for UI interactions, notably through:
    Browser/: Scripts for browser setup and actions, facilitating browser control for tests.
    POM/ (Page Object Models): Defines objects representing web pages or components, encapsulating page-specific properties and methods to interact with them,          promoting code reuse and maintenance.
b). API/: Encapsulates functionality for API testing, including wrappers or utilities to simplify API calls and responses handling.

2.Playground/: It's divided into two main parts:

a). Tests/: Dedicated space for test scripts, segregated into:
    API/: Contains tests focused on API validation, leveraging structures defined in Engine/API/.
    UI/: Comprises tests that interact with the user interface, utilizing tools from Engine/UI/, following the Page Object Model pattern for structured and     
    maintainable test code.
b). Resources/: A repository for auxiliary files that support testing but don't contain test logic or core framework code, divided into:
    API/: Stores configuration files or data related to API testing (e.g., endpoint URLs, request payloads).
    UI/: Holds data and configurations for UI tests, including URLs, test data files, and potentially other resources like element selectors.
```

### Project Architecture Diagram

```
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
```

#### Principles used here:

1. KISS (Keep It Simple, Stupid)
2. AHA (Avoid Hasty Abstractions)
3. Page Object Models
4. Data-Driven Architecture
5. Fluent Pattern



