# c10vis-poem／github-mcp-server: GitHub's official MCP Server

Watch
0
GitHub's official MCP Server
MIT License
Code of conduct
Contributing
Security policy
0 stars
0 forks
0 watching
1 branch
0 tags
Activity
Public repository · Forked from github/github-mcp-server
1 Branch
0 Tags
Go to file
Go to file
Add file
Code
This branch is up to date with github/github-mcp-server:main .
Contribute
Sync fork
3 people
Add batched update_project_items writes via GraphQL (github#2903)
d080b23 · 7 hours ago
.github
fix: bump Node.js from 20 to 22 in build-ui a…
last week
.vscode
Add Streamable HTTP mode (github#1849)
5 months ago
cmd
refactor(auth): isolate GitHub App auth to st…
last week
docs
Make fields parameter available by default (…
13 hours ago
e2e
Add opt-in intent-aware Copilot issue assign…
last week
internal
refactor(auth): isolate GitHub App auth to st…
last week
pkg
Add batched update_project_items writes vi…
7 hours ago
script
perf(octicons): embed precomputed data U…
2 weeks ago
third-party
chore(deps): bump go-github v87 → v89 an…
3 weeks ago
ui
build(deps): bump the npm_and_yarn group …
last week
.dockerignore
Optimize Docker build with bind mounts (git…
last year
.gitignore
chore(gitignore): anchor binary names to re…
2 months ago
.golangci.yml
refactor: modernize code with modernize an…
5 months ago
.goreleaser.yaml
feat(oauth): add stdio OAuth 2.1 login core li…
last month
CODE_OF_CONDUCT.md
chore: move COC to top level
last year
CONTRIBUTING.md
feat: Add Octicon icons to MCP tools, resour…
7 months ago
Dockerfile
build(deps): bump distroless/base-debian12…
last week
LICENSE
Create LICENSE
last year
README.md
Add batched update_project_items writes vi…
7 hours ago
SECURITY.md
docs: add oss documentation
last year
SUPPORT.md
docs: add oss documentation
last year
c10vis-poem
github-mcp-server
Code
Pull requests
Agents
Actions
Projects
Security and quality
Insights
Settings
Fork
0
m
T


gemini-extension.json
Add Gemini CLI extension (github#1232)
9 months ago
go.mod
Bump go-github to pick up SearchType supp…
16 hours ago
go.sum
Bump go-github to pick up SearchType supp…
16 hours ago
server.json
feat(oauth): add stdio OAuth 2.1 login core li…
last month
third-party-licenses.darwin.md
Bump go-github to pick up SearchType supp…
16 hours ago
third-party-licenses.linux.md
Bump go-github to pick up SearchType supp…
16 hours ago
third-party-licenses.windows.md
Bump go-github to pick up SearchType supp…
16 hours ago
go report
go report r e t i r e d
r e t i r e d
The GitHub MCP Server connects AI tools directly to GitHub's platform. This gives AI agents, assistants, and chatbots the ability to read
repositories and code files, manage issues and PRs, analyze code, and automate workflows. All through natural language interactions.
Repository Management: Browse and query code, search files, analyze commits, and understand project structure across any repository
you have access to.
Issue & PR Automation: Create, update, and manage issues and pull requests. Let AI help triage bugs, review code changes, and maintain
project boards.
CI/CD & Workflow Intelligence: Monitor GitHub Actions workflow runs, analyze build failures, manage releases, and get insights into your
development pipeline.
Code Analysis: Examine security findings, review Dependabot alerts, understand code patterns, and get comprehensive insights into your
codebase.
Team Collaboration: Access discussions, manage notifications, analyze team activity, and streamline processes for your team.
Built for developers who want to connect their AI tools to GitHub context and capabilities, from simple natural language queries to complex
multi-step agent workflows.
VS Code Install Server
VS Code Insiders Install Server
Visual Studio Install Server
The remote GitHub MCP Server is hosted by GitHub and provides the easiest method for getting up and running. If your MCP host does not
support remote MCP servers, don't worry! You can use the local version of the GitHub MCP Server instead.
1. A compatible MCP host with remote server support (VS Code 1.101+, Claude Desktop, Cursor, Windsurf, etc.)
2. Any applicable policies enabled
For quick installation, use one of the one-click install buttons above. Once you complete that flow, toggle Agent mode (located by the Copilot
Chat text input) and the server will start. Make sure you're using VS Code 1.101 or later for remote MCP and OAuth support.
Alternatively, to manually configure VS Code, choose the appropriate JSON block from the examples below and add it to your host
configuration:
GitHub MCP Server
Use Cases
Remote GitHub MCP Server
Prerequisites
Install in VS Code
README
Code of conduct
Contributing
License
Security


Using OAuth
Using a GitHub PAT
VS Code (version 1.101 or greater)
Copilot CLI - Installation guide for GitHub Copilot CLI
GitHub Copilot in other IDEs - Installation for JetBrains, Visual Studio, Eclipse, and Xcode with GitHub Copilot
Claude Applications - Installation guide for Claude Desktop and Claude Code CLI
Codex - Installation guide for OpenAI Codex
Cursor - Installation guide for Cursor IDE
OpenCode - Installation guide for the OpenCode terminal agent
Windsurf - Installation guide for Windsurf IDE
Zed - Installation guide for Zed editor
Rovo Dev CLI - Installation guide for Rovo Dev CLI
Note: Each MCP host application needs to configure a GitHub App or OAuth App to support remote access via OAuth. Any host
application that supports remote MCP servers should support the remote GitHub server with PAT authentication. Configuration details
and support levels vary by host. Make sure to refer to the host application's documentation for more info.
See Remote Server Documentation for full details on remote server configuration, toolsets, headers, and advanced usage. This file provides
comprehensive instructions and examples for connecting, customizing, and installing the remote GitHub MCP Server in VS Code and other
MCP hosts.
When no toolsets are specified, default toolsets are used.
Try new features early! The remote server offers an insiders version with early access to new features and experimental tools.
Using URL Path
Using Header
{
  "servers": {
    "github": {
      "type": "http",
      "url": "https://api.githubcopilot.com/mcp/"
    }
  }
}
{
  "servers": {
    "github": {
      "type": "http",
      "url": "https://api.githubcopilot.com/mcp/",
      "headers": {
        "Authorization": "Bearer ${input:github_mcp_pat}"
      }
    }
  },
  "inputs": [
    {
      "type": "promptString",
      "id": "github_mcp_pat",
      "description": "GitHub Personal Access Token",
      "password": true
    }
  ]
}
Install in other MCP hosts
Configuration
Toolset configuration
Insiders Mode
{
  "servers": {
    "github": {
      "type": "http",
      "url": "https://api.githubcopilot.com/mcp/insiders"
    }
{
  "servers": {
    "github": {
      "type": "http",
      "url": "https://api.githubcopilot.com/mcp/",
      "headers": {
        "X-MCP-Insiders": "true"


See Remote Server Documentation for more details and examples, and Insiders Features for a full list of what's available.
GitHub Enterprise Cloud can also make use of the remote server.
Example for https://octocorp.ghe.com with GitHub PAT token:
Note: When using OAuth with GitHub Enterprise with VS Code and GitHub Copilot, you also need to configure your VS Code settings to
point to your GitHub Enterprise instance - see Authenticate from VS Code
GitHub Enterprise Server does not support remote server hosting. Please refer to GitHub Enterprise Server and Enterprise Cloud with data
residency (ghe.com) from the local server configuration.
VS Code Install Server
VS Code Insiders Install Server
Visual Studio Install Server
1. To run the server in a container, you will need to have Docker installed.
2. Once Docker is installed, you will also need to ensure Docker is running. The Docker image is available at ghcr.io/github/github-mcp-
server . The image is public; if you get errors on pull, you may have an expired token and need to docker logout ghcr.io .
3. Authentication. On github.com you don't need to create anything up front — the one-click buttons above log you in with OAuth on first use
(a browser-based flow; the token is kept in memory only). The Docker buttons publish a fixed callback port ( 127.0.0.1:8085 ) so the
container's login callback is reachable. See Local Server OAuth Login for how it works, headless/device-code fallback, and bringing your
own OAuth or GitHub App (required for GitHub Enterprise Server and ghe.com ).
Prefer a token? You can still authenticate with a GitHub Personal Access Token by setting GITHUB_PERSONAL_ACCESS_TOKEN instead (it
takes precedence over OAuth). The MCP server can use many of the GitHub APIs, so enable the permissions that you feel comfortable
granting your AI tools (to learn more about access tokens, please check out the documentation).
Handling PATs Securely
The flag --gh-host and the environment variable GITHUB_HOST can be used to set the hostname for GitHub Enterprise Server or GitHub
Enterprise Cloud with data residency.
  }
}
      }
    }
  }
}
GitHub Enterprise
GitHub Enterprise Cloud with data residency (ghe.com)
{
    ...
    "github-octocorp": {
      "type": "http",
      "url": "https://copilot-api.octocorp.ghe.com/mcp",
      "headers": {
        "Authorization": "Bearer ${input:github_mcp_pat}"
      }
    },
    ...
}
GitHub Enterprise Server
Local GitHub MCP Server
Prerequisites
GitHub Enterprise Server and Enterprise Cloud with data residency (ghe.com)


For GitHub Enterprise Server, prefix the hostname with the https:// URI scheme, as it otherwise defaults to http:// , which GitHub
Enterprise Server does not support.
For GitHub Enterprise Cloud with data residency, use https://YOURSUBDOMAIN.ghe.com as the hostname.
For quick installation, use one of the one-click install buttons above. Once you complete that flow, toggle Agent mode (located by the Copilot
Chat text input) and the server will start.
More about using MCP server tools in VS Code's agent mode documentation.
Install in GitHub Copilot on other IDEs (JetBrains, Visual Studio, Eclipse, etc.)
Add one of the following JSON blocks to your IDE's MCP settings.
Log in with OAuth (no token to create or store). On github.com the official image already includes the app credentials, so you provide none
yourself: it runs a browser-based login on first use and keeps the resulting token in memory only. In Docker this needs a fixed callback port
published to loopback so the container's login callback is reachable:
See Local Server OAuth Login for the native-binary flow (no fixed port needed), the headless/device-code fallback, GitHub Enterprise Server /
ghe.com , and bringing your own OAuth or GitHub App.
For non-interactive stdio deployments, see GitHub App Authentication.
"github": {
    "command": "docker",
    "args": [
    "run",
    "-i",
    "--rm",
    "-e",
    "GITHUB_PERSONAL_ACCESS_TOKEN",
    "-e",
    "GITHUB_HOST",
    "ghcr.io/github/github-mcp-server"
    ],
    "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "${input:github_token}",
        "GITHUB_HOST": "https://<your GHES or ghe.com domain name>"
    }
}
Installation
Install in GitHub Copilot on VS Code
{
  "mcp": {
    "servers": {
      "github": {
        "command": "docker",
        "args": [
          "run",
          "-i",
          "--rm",
          "-p",
          "127.0.0.1:8085:8085",
          "-e",
          "GITHUB_OAUTH_CALLBACK_PORT",
          "ghcr.io/github/github-mcp-server"
        ],
        "env": {
          "GITHUB_OAUTH_CALLBACK_PORT": "8085"
        }
      }
    }
  }
}


Or authenticate with a Personal Access Token. Set GITHUB_PERSONAL_ACCESS_TOKEN instead (it takes precedence over OAuth):
Optionally, you can add a similar example (i.e. without the mcp key) to a file called .vscode/mcp.json in your workspace. This will allow you t
share the configuration with other host applications that accept the same format.
Example JSON block without the MCP key included
For other MCP host applications, please refer to our installation guides:
Copilot CLI - Installation guide for GitHub Copilot CLI
GitHub Copilot in other IDEs - Installation for JetBrains, Visual Studio, Eclipse, and Xcode with GitHub Copilot
Claude Code & Claude Desktop - Installation guide for Claude Code and Claude Desktop
Cursor - Installation guide for Cursor IDE
Google Gemini CLI - Installation guide for Google Gemini CLI
OpenCode - Installation guide for the OpenCode terminal agent
Windsurf - Installation guide for Windsurf IDE
Zed - Installation guide for Zed editor
For a complete overview of all installation options, see our Installation Guides Index.
Note: Any host application that supports local MCP servers should be able to access the local GitHub MCP server. However, the specific
configuration process, syntax and stability of the integration will vary by host application. While many may follow a similar format to the
examples above, this is not guaranteed. Please refer to your host application's documentation for the correct MCP configuration syntax
and setup process.
If you don't have Docker, you can use go build to build the binary in the cmd/github-mcp-server directory, and use the github-mcp-server
stdio command with the GITHUB_PERSONAL_ACCESS_TOKEN environment variable set to your token. To specify the output location of the build
use the -o flag. You should configure your server to use the built executable as its command . For example:
{
  "mcp": {
    "inputs": [
      {
        "type": "promptString",
        "id": "github_token",
        "description": "GitHub Personal Access Token",
        "password": true
      }
    ],
    "servers": {
      "github": {
        "command": "docker",
        "args": [
          "run",
          "-i",
          "--rm",
          "-e",
          "GITHUB_PERSONAL_ACCESS_TOKEN",
          "ghcr.io/github/github-mcp-server"
        ],
        "env": {
          "GITHUB_PERSONAL_ACCESS_TOKEN": "${input:github_token}"
        }
      }
    }
  }
}
Install in Other MCP Hosts
Build from source
{
  "mcp": {
    "servers": {


The github-mcp-server binary includes a few CLI subcommands that are helpful for debugging and exploring the server.
github-mcp-server tool-search "<query>" searches tools by name, description, and input parameter names. Use --max-results to
return more matches. Example (color output requires a TTY; use docker run -t (or -it ) when running in Docker):
The GitHub MCP Server supports enabling or disabling specific groups of functionalities via the --toolsets flag. This allows you to control
which GitHub API capabilities are available to your AI tools. Enabling only the toolsets that you need can help the LLM with tool choice and
reduce the context size.
Toolsets are not limited to Tools. Relevant MCP Resources and Prompts are also included where applicable.
When no toolsets are specified, default toolsets are used.
Looking for examples? See the Server Configuration Guide for common recipes like minimal setups, read-only mode, and combining tools
with toolsets.
To specify toolsets you want available to the LLM, you can pass an allow-list in two ways:
1. Using Command Line Argument:
2. Using Environment Variable:
The environment variable GITHUB_TOOLSETS takes precedence over the command line argument if both are provided.
You can also configure specific tools using the --tools flag. Tools can be used independently or combined with toolsets for fine-grained
control.
1. Using Command Line Argument:
2. Using Environment Variable:
      "github": {
        "command": "/path/to/github-mcp-server",
        "args": ["stdio"],
        "env": {
          "GITHUB_PERSONAL_ACCESS_TOKEN": "<YOUR_TOKEN>"
        }
      }
    }
  }
}
CLI utilities
docker run -it --rm ghcr.io/github/github-mcp-server tool-search "issue" --max-results 5
github-mcp-server tool-search "issue" --max-results 5
Tool Configuration
Specifying Toolsets
github-mcp-server --toolsets repos,issues,pull_requests,actions,code_security
GITHUB_TOOLSETS="repos,issues,pull_requests,actions,code_security" ./github-mcp-server
Specifying Individual Tools
github-mcp-server --tools get_file_contents,issue_read,create_pull_request
GITHUB_TOOLS="get_file_contents,issue_read,create_pull_request" ./github-mcp-server


3. Combining with Toolsets (additive):
This registers all tools from repos and issues toolsets, plus get_gist .
Important Notes:
Tools and toolsets can be used together
Read-only mode takes priority: write tools are skipped if --read-only is set, even if explicitly requested via --tools
Tool names must match exactly (e.g., get_file_contents , not getFileContents ). Invalid tool names will cause the server to fail at
startup with an error message
When tools are renamed, old names are preserved as aliases for backward compatibility. See Tool Renaming for details.
When using Docker, you can pass the toolsets as environment variables:
When using Docker, you can pass specific tools as environment variables. You can also combine tools with toolsets:
The special toolset all can be provided to enable all available toolsets regardless of any other configuration:
Or using the environment variable:
The default toolset default is the configuration that gets passed to the server if no toolsets are specified.
The default configuration is:
context
repos
issues
github-mcp-server --toolsets repos,issues --tools get_gist
Using Toolsets With Docker
docker run -i --rm \
  -e GITHUB_PERSONAL_ACCESS_TOKEN=<your-token> \
  -e GITHUB_TOOLSETS="repos,issues,pull_requests,actions,code_security" \
  ghcr.io/github/github-mcp-server
Using Tools With Docker
# Tools only
docker run -i --rm \
  -e GITHUB_PERSONAL_ACCESS_TOKEN=<your-token> \
  -e GITHUB_TOOLS="get_file_contents,issue_read,create_pull_request" \
  ghcr.io/github/github-mcp-server
# Tools combined with toolsets (additive)
docker run -i --rm \
  -e GITHUB_PERSONAL_ACCESS_TOKEN=<your-token> \
  -e GITHUB_TOOLSETS="repos,issues" \
  -e GITHUB_TOOLS="get_gist" \
  ghcr.io/github/github-mcp-server
Special toolsets
"all" toolset
./github-mcp-server --toolsets all
GITHUB_TOOLSETS="all" ./github-mcp-server
"default" toolset


pull_requests
users
To keep the default configuration and add additional toolsets:
The local GitHub MCP Server offers an insiders version with early access to new features and experimental tools.
1. Using Command Line Argument:
2. Using Environment Variable:
When using Docker:
The following sets of tools are available:
Toolset
Description
context
Strongly recommended: Tools that provide context about the current user and GitHub context you are
operating in
actions
GitHub Actions workflows and CI/CD operations
code_quality
GitHub Code Quality related tools
code_security
Code security related tools, such as GitHub Code Scanning
copilot
Copilot related tools
copilot_issue_intents
Opt-in Copilot issue assignment tools that carry intent metadata (rationale, confidence, suggestion)
dependabot
Dependabot tools
discussions
GitHub Discussions related tools
gists
GitHub Gist related tools
git
GitHub Git API related tools for low-level Git operations
issues
GitHub Issues related tools
labels
GitHub Labels related tools
notifications
GitHub Notifications related tools
orgs
GitHub Organization related tools
projects
GitHub Projects related tools
pull_requests
GitHub Pull Request related tools
GITHUB_TOOLSETS="default,stargazers" ./github-mcp-server
Insiders Mode
./github-mcp-server --insiders
GITHUB_INSIDERS=true ./github-mcp-server
docker run -i --rm \
  -e GITHUB_PERSONAL_ACCESS_TOKEN=<your-token> \
  -e GITHUB_INSIDERS=true \
  ghcr.io/github/github-mcp-server
Available Toolsets


Toolset
Description
repos
GitHub Repository related tools
secret_protection
Secret protection related tools, such as GitHub Secret Scanning
security_advisories
Security advisories related tools
stargazers
GitHub Stargazers related tools
users
GitHub User related tools
Toolset
Description
copilot
Copilot related tools (e.g. Copilot Coding Agent)
copilot_spaces
Copilot Spaces related tools
github_support_docs_search
Search docs to answer GitHub product and support questions
 Actions
 Code Quality
 Code Security
 Context
 Copilot
 Copilot Issue Intents
 Dependabot
 Discussions
 Gists
 Git
 Issues
 Labels
 Notifications
 Organizations
 Projects
 Pull Requests
 Repositories
 Secret Protection
 Security Advisories
 Stargazers
 Users
Additional Toolsets in Remote GitHub MCP Server
Tools


Copilot
Copilot Spaces
GitHub Support Docs Search
To run the server in read-only mode, you can use the --read-only flag. This will only offer read-only tools, preventing any modifications to
repositories, issues, pull requests, etc.
When using Docker, you can pass the read-only mode as an environment variable:
Lockdown mode limits the content that the server will surface from public repositories. When enabled, the server checks whether the author of
each item has push access to the repository. Private repositories are unaffected, and collaborators keep full access to their own content.
When running with Docker, set the corresponding environment variable:
The behavior of lockdown mode depends on the tool invoked.
Following tools will return an error when the author lacks the push access:
issue_read:get
pull_request_read:get
Following tools will filter out content from users lacking the push access:
issue_read:get_comments
issue_read:get_sub_issues
pull_request_read:get_comments
pull_request_read:get_review_comments
pull_request_read:get_reviews
The descriptions of the tools can be overridden by creating a github-mcp-server-config.json file in the same directory as the binary.
The file should contain a JSON object with the tool names as keys and the new descriptions as values. For example:
Additional Tools in Remote GitHub MCP Server
Read-Only Mode
./github-mcp-server --read-only
docker run -i --rm \
  -e GITHUB_PERSONAL_ACCESS_TOKEN=<your-token> \
  -e GITHUB_READ_ONLY=1 \
  ghcr.io/github/github-mcp-server
Lockdown Mode
./github-mcp-server --lockdown-mode
docker run -i --rm \
  -e GITHUB_PERSONAL_ACCESS_TOKEN=<your-token> \
  -e GITHUB_LOCKDOWN_MODE=1 \
  ghcr.io/github/github-mcp-server
i18n / Overriding Descriptions
{
  "TOOL_ADD_ISSUE_COMMENT_DESCRIPTION": "an alternative description",


You can create an export of the current translations by running the binary with the --export-translations flag.
This flag will preserve any translations/overrides you have made, while adding any new translations that have been added to the binary since
the last time you exported.
You can also use ENV vars to override the descriptions. The environment variable names are the same as the keys in the JSON file, prefixed
with GITHUB_MCP_ and all uppercase.
For example, to override the TOOL_ADD_ISSUE_COMMENT_DESCRIPTION tool, you can set the following environment variable:
The same override mechanism can be used to customize the MCP server's name and title fields in the initialization response. This is usefu
when running multiple GitHub MCP Server instances (e.g., one for github.com and one for GitHub Enterprise Server) so that agents can
distinguish between them.
Key
Environment Variable
Default
SERVER_NAME
GITHUB_MCP_SERVER_NAME
github-mcp-server
SERVER_TITLE
GITHUB_MCP_SERVER_TITLE
GitHub MCP Server
For example, to configure a server instance for GitHub Enterprise Server:
Or using environment variables:
The exported Go API of this module should currently be considered unstable, and subject to breaking changes. In the future, we may offer
stability; please file an issue if there is a use case where this would be valuable.
Contributions are welcome. Before opening a pull request, please read the contributing guide for setup, testing, linting, and documentation
generation instructions.
For help using the GitHub MCP Server, see the support guide. If you have found a bug or want to request a feature, please search existing
issues before opening a new one.
  "TOOL_CREATE_BRANCH_DESCRIPTION": "Create a new branch in a GitHub repository"
}
./github-mcp-server --export-translations
cat github-mcp-server-config.json
export GITHUB_MCP_TOOL_ADD_ISSUE_COMMENT_DESCRIPTION="an alternative description"
Overriding Server Name and Title
{
  "SERVER_NAME": "ghes-mcp-server",
  "SERVER_TITLE": "GHES MCP Server"
}
export GITHUB_MCP_SERVER_NAME="ghes-mcp-server"
export GITHUB_MCP_SERVER_TITLE="GHES MCP Server"
Library Usage
Contributing
Support
Security


Releases
No releases published
Create a new release
Packages
No packages published
Publish your first package
Contributors
No contributors
Languages
Go 94%
TypeScript 4.7%
Other 1.3%
Suggested workflows
Based on your tech stack
Go
Build a Go project.
By GitHub Actions
Configure
SLSA Go releaser
Compile your Go project using a SLSA3 compliant builder
By Open Source Security Foundation (OpenSSF)
Configure
SLSA Generic generator
Generate SLSA3 provenance for your existing release workflows
By Open Source Security Foundation (OpenSSF)
Configure
More workflows
