# Streamlit Web Application Development Guidelines

This document provides essential information for AI agents working with this Streamlit-based web application project.

## Project Overview
This is a Streamlit web application that provides a simple user interface for basic mathematical operations. The application is built using Python and Streamlit framework.

### Key Components
- Main application file: `app.py` - Contains all UI components and business logic
- Technology stack: Python with Streamlit framework

## Development Patterns

### UI Component Structure
- Use Streamlit's built-in components for UI elements
- Layout organized using column system (`st.columns`)
- Input components placed in separate columns for better organization
- Result display using `st.success()` for positive feedback

### Common Patterns
1. **Layout Management**:
   ```python
   c1, c2 = st.columns(2)  # Create two-column layout
   c1.number_input(...)    # Place components in specific columns
   ```

2. **User Input Handling**:
   - Use appropriate Streamlit input widgets based on data type
   - Number inputs include validation (`min_value`, `max_value`, `step`)

3. **Action Triggers**:
   - Use `st.button()` for action triggers
   - Place response logic within button conditional blocks

## Development Workflow

### Running the Application
To run the application locally:
1. Ensure Streamlit is installed
2. Run `streamlit run app.py` from the project directory

### Adding New Features
When adding new features:
1. Place UI components logically within the existing layout
2. Group related inputs using columns when appropriate
3. Include clear success/error messages for user feedback

## Best Practices
1. Keep all UI components in `app.py` for this simple application
2. Use Streamlit's built-in formatting for consistent appearance
3. Implement user feedback for all actions using appropriate message types
   - Success messages: `st.success()`
   - Error messages: `st.error()`
   - Info messages: `st.info()`

## Integration Points
- The application is self-contained with Streamlit as the only external dependency
- Future integrations should be added as separate functions in `app.py`