
# VS Code

# Set the fucking python interpreter.  


Method 1: Using the Command Palette (Recommended)

1. Open your project folder in VS Code.
2. Press Ctrl + Shift + P (Windows/Linux) or Cmd + Shift + P (macOS) to open the Command Palette.
3. Type Python: Select Interpreter and select it from the list.
4. Choose your preferred Python version or virtual environment from the detected list.

# Test Framework
To set your testing framework to pytest in Visual Studio Code, make sure you have the official Python extension installed, open your project folder, and use the built-in configuration tool.

Method 1: Using the Command Palette (Recommended)

1. Open the Command Palette by pressing Ctrl + Shift + P (Windows/Linux) or Cmd + Shift + P (Mac).
2. Type and select Python: Configure Tests.
3. Choose pytest from the framework list.
4. Select your root directory or the specific folder containing your test files (e.g., . for root or tests/).

Method 2: Using the Testing Sidebar

1. Click the Testing icon (looks like a laboratory beaker) on the left Activity Bar.
2. Click the Configure Python Tests button.
3. Select pytest and specify your test folder.

Method 3: Direct Manual Configuration

Alternatively, you can manually configure your project by editing or creating a .vscode/settings.json file in your workspace directory:
json
{
    "python.testing.unittestEnabled": false,
    "python.testing.pytestEnabled": true,
    "python.testing.pytestArgs": [
        "tests"
    ]
}

# Create a run configuration - you need this for the debugger

To create a debug run configuration in Visual Studio Code, you need to generate a launch.json file inside your project's .vscode folder. This file stores your custom run and environment settings.

Step-by-Step Guide

1. Open your project folder in VS Code (File > Open Folder...).
2. Click the Run and Debug icon in the Activity Bar on the side of VS Code (or press Ctrl+Shift+D on Windows/Linux or Cmd+Shift+D on macOS).
3. Click the link that says create a launch.json file.
4. A dropdown menu will appear at the top of the window. Select the environment/debugger that matches your language or runtime (e.g., Node.js, Python, C++, Java).
VS Code will automatically generate a .vscode/launch.json file with a baseline configuration.

Understanding the Configuration Parameters

When you open your new launch.json file, you will see a structured layout of parameters within a configurations array:
json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Launch Program",
      "type": "node",
      "request": "launch",
      "program": "${workspaceFolder}/app.js",
      "args": ["--port", "8080"],
      "env": { "NODE_ENV": "development" }
    }
  ]
}
Use code with caution.
• name: The reader-friendly name that shows up in the debug dropdown menu.
• type: The debugger extension to use (e.g., node, python, cppdbg).
• request: Either launch (starts the application fresh) or attach (connects to an already running external process).
• program: The main file or entry point path executable to execute when launching the debugger.
• args: An array of command-line arguments to pass to your program during initialization.
• env: Object containing environment variables to inject exclusively into the debug environment.

Adding Multiple Configurations

If you want to add an alternate setup (e.g., a test suite runner alongside your main app runtime):
1. Open your existing launch.json file.
2. Click the Add Configuration... button that appears in the bottom-right corner of the editor area.
3. Choose the new snippet option from the context menu to append it directly to your configuration settings array.


# NVIDIA
NVIDIA Alt-Z to access some stuff about that
Version 581.57 (Tue Oct 14, 2025) Studio Driver
