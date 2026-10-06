# DevO Auto Setup - Automatic Repository Setup with AI

## 🚀 **Overview**

The DevO Auto Setup feature automatically handles repository cloning, dependency installation, error detection, and fixing - all powered by AI. When you provide a repository URL, the system does all the heavy lifting to get you up and running quickly.

## ✨ **Key Features**

### 🔄 **Fully Automated Process**
- **Repository Cloning**: Automatically clones from any git URL
- **Language Detection**: Identifies Python, Node.js, and other languages
- **Framework Detection**: Recognizes Flask, Django, React, Next.js, etc.
- **Dependency Installation**: Uses appropriate package managers (pip, npm, yarn)
- **Error Correction**: AI-powered automatic fix for common issues
- **Validation**: Ensures setup is working correctly
- **Reporting**: Comprehensive setup report with next steps

### 🤖 **AI-Powered Error Fixing**
- **Dependency Conflicts**: Automatically resolves version conflicts
- **Missing Dependencies**: Installs missing packages detected in imports
- **Syntax Errors**: AI analyzes and fixes basic syntax issues
- **Configuration Issues**: Creates missing essential files
- **Import Errors**: Resolves import path and module issues

### 📊 **Smart Analysis**
- **Project Structure**: Understands project layout and organization
- **Package Managers**: Detects and uses pip, npm, yarn, pnpm, poetry
- **Build Systems**: Handles various build configurations
- **Environment Setup**: Creates appropriate virtual environments

## 🎯 **How to Use**

### **Method 1: Through Chat Interface**
```bash
# Start DevO Chat
uv run python chat.py

# In the chat, use the setup command
You: setup https://github.com/user/awesome-project.git
```

### **Method 2: Direct Command Line**
```bash
# Use the standalone auto setup script
uv run python auto_setup.py https://github.com/user/awesome-project.git

# Or use the Windows batch file
.\auto_setup.bat https://github.com/user/awesome-project.git
```

### **Method 3: With Custom Target Directory**
```bash
# Specify where to clone the repository
uv run python auto_setup.py https://github.com/user/project.git --target-dir ./my-projects
```

## 🔧 **What Gets Done Automatically**

### **1. Repository Cloning**
```
📥 Cloning repository...
   ✅ Repository cloned to: ./awesome-project
```

### **2. Project Analysis**
```
📊 Repository Analysis Complete
   Language: python
   Framework: flask
   Package Manager: pip
```

### **3. Environment Setup**
```
🔧 Setting up python environment...
   ✅ uv project initialized
   ✅ Dependencies installed
   ✅ Development tools added
```

### **4. Error Detection & Fixing**
```
🔍 Detecting and fixing errors...
   ✅ Import errors resolved
   ✅ Missing dependencies installed
   ✅ Syntax errors fixed
   ✅ Configuration files created
```

### **5. Validation**
```
🎯 Setup validation complete
   ✅ Environment ready
   ✅ Dependencies working
   ✅ Project structure validated
```

## 🛠️ **AI-Powered Problem Solving**

### **Dependency Issues**
When the system encounters dependency problems:
1. **Analyzes** the error output with AI
2. **Identifies** root causes (version conflicts, missing packages)
3. **Generates** specific fix commands
4. **Executes** the fixes automatically
5. **Validates** the solution worked

### **Example Auto-Fix**
```
⚠️ Dependency installation issues detected
🤖 AI analyzing dependency errors...

AI Analysis:
The error indicates a version conflict between Flask 2.0 and Werkzeug 3.0.
Recommended fixes:
1. Pin Flask to compatible version: uv add "flask>=2.0,<3.0"
2. Downgrade Werkzeug: uv add "werkzeug>=2.0,<3.0"

🔧 Executing: uv add "flask>=2.0,<3.0"
✅ Command successful
```

### **Syntax Error Fixing**
```
❌ Syntax error in app.py
🤖 AI fixing syntax error...

Fixed Issues:
- Missing colon in function definition
- Incorrect indentation in class method
- Updated import statements

✅ Fixed syntax error in app.py
```

## 📋 **Supported Project Types**

### **Python Projects**
- **Flask** applications
- **Django** projects
- **FastAPI** services
- **General Python** scripts and packages
- **Package Managers**: pip, poetry, pipenv

### **Node.js Projects**
- **React** applications
- **Next.js** projects
- **Vue.js** applications
- **Express.js** servers
- **Package Managers**: npm, yarn, pnpm

### **Auto-Detection Features**
- **Language**: Based on file extensions and config files
- **Framework**: Analyzes imports and dependencies
- **Package Manager**: Checks for lock files and configurations
- **Build System**: Detects build tools and configurations

## 📁 **Files Created/Modified**

### **Essential Files Added**
- `requirements.txt` (Python projects)
- `README.md` (if missing)
- `.gitignore` (language-specific)
- `pyproject.toml` (for uv projects)

### **Configuration Updates**
- Package manager files updated
- Development dependencies added
- Build configurations optimized
- Environment variables configured

## 🎯 **Success Validation**

The system validates setup success by:
- **Environment Testing**: Verifies Python/Node can run
- **Dependency Checking**: Confirms all packages are installed
- **Import Testing**: Validates all imports work correctly
- **Build Testing**: Ensures project can be built (if applicable)

## 📈 **Progress Tracking**

Real-time progress indicators show:
```
🔍 Checking uv availability...     ✅
🔧 Initializing uv project...      ✅
📦 Installing dependencies...      ✅
🔍 Detecting errors...            ✅
🤖 AI fixing issues...            ✅
🎯 Validating setup...            ✅
```

## 🚨 **Error Handling**

### **Common Issues Handled**
- **Network Problems**: Retries and fallback strategies
- **Permission Issues**: Suggests solutions for Windows/Linux
- **Version Conflicts**: AI-powered resolution
- **Missing Tools**: Clear installation instructions
- **Corrupted Files**: Re-download and fix

### **Graceful Fallbacks**
- If AI is unavailable, provides manual fix suggestions
- If auto-fix fails, shows detailed error information
- If setup fails, provides rollback options

## 🎉 **Example Workflow**

```bash
# Start the process
You: setup https://github.com/awesome-dev/flask-api.git

# System responds:
🚀 Starting auto setup for: https://github.com/awesome-dev/flask-api.git
📥 Cloning repository...          ✅
📊 Repository Analysis Complete
   Language: python
   Framework: flask
   Package Manager: pip

🔧 Setting up python environment...
   ✅ uv project initialized
   ✅ Dependencies installed

🔍 Detecting and fixing errors...
   ✅ Missing package 'requests' installed
   ✅ Import error in api.py fixed

🎯 Auto Setup Report
   Repository    ✅ Cloned
   Language      ✅ Detected (python)
   Framework     ✅ Detected (flask)
   Dependencies  ✅ Installed
   Validation    ✅ Passed

🎉 Setup Complete! Next Steps:
1. Navigate to project: cd flask-api
2. Start development: Use your preferred IDE
3. Run the project: Check README.md for instructions
4. Chat with DevO: Use `uv run python chat.py` for AI assistance
```

## 🔑 **Configuration Options**

### **Environment Variables**
```bash
# Set API key for AI features
export GROQ_API_KEY=your_api_key_here

# Or create .env file
echo "GROQ_API_KEY=your_api_key_here" > .env
```

### **Command Line Options**
```bash
# Basic usage
uv run python auto_setup.py <repo_url>

# With custom directory
uv run python auto_setup.py <repo_url> --target-dir ./projects

# With specific API key
uv run python auto_setup.py <repo_url> --api-key your_key
```

## 🎁 **Benefits**

✅ **Save Time**: No manual setup procedures  
✅ **Reduce Errors**: AI-powered error detection and fixing  
✅ **Learn**: See how problems are solved automatically  
✅ **Consistency**: Same setup process for all projects  
✅ **Reliability**: Comprehensive validation and reporting  
✅ **Flexibility**: Works with various languages and frameworks  

## 🔄 **Integration with DevO Chat**

After auto setup completes:
- Repository is available for chat analysis
- AI has full context of the project
- Can immediately start asking questions
- All development assistance features are available

The auto setup feature transforms the traditional manual setup process into a seamless, AI-powered experience that gets you coding faster! 🚀
