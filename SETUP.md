# VS Code Setup Guide

This guide will help you set up the Instagram Clone project in VS Code with all the necessary extensions and configurations.

## Prerequisites

Make sure you have these installed:

- **Python 3.8+** - [Download here](https://www.python.org/downloads/)
- **Node.js 16+** - [Download here](https://nodejs.org/)
- **VS Code** - [Download here](https://code.visualstudio.com/)
- **Git** - [Download here](https://git-scm.com/)

## VS Code Extensions

Install these recommended extensions:

### Essential Extensions

1. **Python** (ms-python.python) - Python language support
2. **ES7+ React/Redux/React-Native snippets** (dsznajder.es7-react-js-snippets) - React snippets
3. **Prettier - Code formatter** (esbenp.prettier-vscode) - Code formatting
4. **Auto Rename Tag** (formulahendry.auto-rename-tag) - HTML/JSX tag renaming
5. **Bracket Pair Colorizer** (coenraads.bracket-pair-colorizer) - Bracket highlighting

### Helpful Extensions

6. **GitLens** (eamodio.gitlens) - Enhanced Git capabilities
7. **Thunder Client** (rangav.vscode-thunder-client) - API testing
8. **Django** (batisteo.vscode-django) - Django template support
9. **JavaScript (ES6) code snippets** (xabikos.javascriptsnippets) - JS snippets
10. **Path Intellisense** (christian-kohler.path-intellisense) - File path autocomplete

## Quick Setup

### Option 1: Automated Setup

```bash
# Clone the repository
git clone <your-repo-url>
cd instagram-clone

# Install all dependencies
npm run setup

# Run database migrations
npm run migrate

# Start both servers
npm run dev
```

### Option 2: Manual Setup

1. **Backend Setup**

   ```bash
   cd instagram_project
   pip install -r requirements.txt
   python manage.py makemigrations
   python manage.py migrate
   python manage.py runserver
   ```

2. **Frontend Setup** (in new terminal)
   ```bash
   cd instagram-frontend
   npm install
   npm start
   ```

## VS Code Features

### Debugging

- Press `F5` to start debugging
- Choose "Launch Full Stack" to run both Django and React
- Set breakpoints in Python or JavaScript code

### Tasks

- `Ctrl+Shift+P` → "Tasks: Run Task"
- Available tasks:
  - Django Migrate
  - Django Makemigrations
  - Install Backend Dependencies
  - Install Frontend Dependencies

### Integrated Terminal

- `Ctrl+`` (backtick) to open terminal
- Multiple terminals for backend/frontend
- Automatic virtual environment activation

### Code Navigation

- `Ctrl+Click` on imports to navigate to files
- `Ctrl+Shift+O` to navigate to symbols in file
- `Ctrl+T` to search for files across project

## Project Structure in VS Code

```
instagram-clone/
├── .vscode/                 # VS Code configuration
│   ├── settings.json       # Editor settings
│   ├── launch.json         # Debug configuration
│   └── tasks.json          # Task definitions
├── instagram_project/       # Django backend
│   ├── instagram_app/      # Main Django app
│   ├── manage.py           # Django management
│   └── requirements.txt    # Python dependencies
├── instagram-frontend/      # React frontend
│   ├── src/               # React source code
│   ├── public/            # Static files
│   └── package.json       # Node dependencies
├── .gitignore             # Git ignore rules
├── package.json           # Root package.json for scripts
└── README.md              # Project documentation
```

## Development Workflow

### Daily Development

1. Open VS Code in project root
2. Press `F5` to start both servers
3. Make changes to code
4. Use `Ctrl+S` to save (auto-formats code)
5. Test changes in browser

### Making Database Changes

1. Modify models in `instagram_project/instagram_app/models.py`
2. Run task: "Django Makemigrations"
3. Run task: "Django Migrate"
4. Restart Django server

### Adding New Features

1. Create new React components in `instagram-frontend/src/components/`
2. Add new API endpoints in `instagram_project/instagram_app/`
3. Update URLs in respective `urls.py` files
4. Test with Thunder Client extension

## Troubleshooting

### Python Issues

- Make sure Python interpreter is set correctly
- Check if virtual environment is activated
- Verify all packages are installed: `pip list`

### Node.js Issues

- Clear npm cache: `npm cache clean --force`
- Delete node_modules and reinstall: `rm -rf node_modules && npm install`
- Check Node version: `node --version`

### VS Code Issues

- Reload window: `Ctrl+Shift+P` → "Developer: Reload Window"
- Check extension conflicts
- Reset VS Code settings if needed

## Useful Shortcuts

### General

- `Ctrl+Shift+P` - Command Palette
- `Ctrl+`` - Toggle Terminal
- `Ctrl+B` - Toggle Sidebar
- `F5` - Start Debugging

### Editing

- `Alt+Up/Down` - Move line up/down
- `Shift+Alt+Up/Down` - Copy line up/down
- `Ctrl+D` - Select next occurrence
- `Ctrl+Shift+L` - Select all occurrences

### Navigation

- `Ctrl+P` - Quick file open
- `Ctrl+Shift+O` - Go to symbol
- `Ctrl+G` - Go to line
- `F12` - Go to definition

## Git Integration

VS Code has built-in Git support:

- View changes in Source Control panel (`Ctrl+Shift+G`)
- Stage changes by clicking `+` next to files
- Commit with message in text box
- Push/pull using status bar buttons

## API Testing

Use Thunder Client extension:

1. Install Thunder Client extension
2. Create new request
3. Set URL to `http://localhost:8000/api/...`
4. Add Authorization header: `Bearer <your-jwt-token>`
5. Test your API endpoints

This setup gives you a complete development environment for the Instagram Clone project!
