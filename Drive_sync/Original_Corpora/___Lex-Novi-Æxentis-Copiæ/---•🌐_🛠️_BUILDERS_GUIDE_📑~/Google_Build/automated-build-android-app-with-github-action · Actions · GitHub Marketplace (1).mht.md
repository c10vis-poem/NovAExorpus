# automated-build-android-app-with-github-action · Actions · GitHub Marketplace (1)

# automated-build-android-app-with-github-action

Actions## Tags

(2)- Available on Google Dev Library [Click Here](https://devlibrary.withgoogle.com/products/android/repos/amirisback-automated-build-android-app-with-github-action)
- Project Github Action Script YAML
- Using Github Workflows
- Automated Build AAB (release)
- Automated Build APK (release and debug)
- Have Bundle Tool
- Download Artifact
- Upload Artifact
- Clear (Artifact naming)
- Sample Naming : ${date_today} - ${repository_name} - ${playstore_name} - APK(s) release generated
- Private Repository Tested (Passed Build App bundle(s) and APK generated successfully)
- Local Run With .run configuration in Local Machine
- Full Code For Github Action Workflows [Click Here](https://github.com/amirisback/automated-build-android-app-with-github-action/blob/master/.github/workflows/generate-apk-aab-debug-release.yml)

This Is Latest Release

```
$version_release = 2.2.7
```
What's New??

```
* Update Target SDK 36 *
* Update Action Script *
* Update Android Studio Latest Version *
* Update Gradle Latest Version *
* Update Kotlin Latest Version *
* Update Github Action Script *
* Add Bash and Bat Script *
```
- [How To Securely Build and Sign Your Android App With GitHub Actions](https://proandroiddev.com/how-to-securely-build-and-sign-your-android-app-with-github-actions-ad5323452ce)
- [How to Use GitHub Actions to Automate Android App Development](https://www.freecodecamp.org/news/use-github-actions-to-automate-android-development/)
- [Update Java Checkout Version CI](https://github.com/actions/setup-java)

- Project must be android studio project using gradle

- Create Files with name generate-apk-aab-debug-release.yml inside folder .github/workflows/
- .github/workflows/generate-apk-aab-debug-release.yml this is position files

```
name: Generated APK AAB (Push Github - Create Artifact To Github Action)
env:
  # The name of the main module repository
  main_project_module: app
  # The name of the Play Store
  playstore_name: Frogobox ID
  # The output folder for build results
  build_output_path: buildActionResult
on:
  push:
    branches:
      - 'release/**'
  # Allows you to run this workflow manually from the Actions tab
  workflow_dispatch:
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      # Set Current Date As Env Variable
      - name: Set current date as env variable
        run: echo "date_today=$(date +'%Y-%m-%d')" >> $GITHUB_ENV
      # Set Repository Name As Env Variable
      - name: Set repository name as env variable
        run: echo "repository_name=$(echo '${{ github.repository }}' | awk -F '/' '{print $2}')" >> $GITHUB_ENV
      - name: Set Up JDK
        uses: actions/setup-java@v4
        with:
          distribution: 'zulu' # See 'Supported distributions' for available options
          java-version: '17'
          cache: 'gradle'
      - name: Change wrapper permissions
        run: chmod +x ./gradlew
      # Run Tests Build
      - name: Run gradle tests
        run: ./gradlew test
      # Run Build Project
      - name: Build gradle project
        run: ./gradlew build
      # Create APK Debug
      - name: Build apk debug project (APK) - ${{ env.main_project_module }} module
        run: ./gradlew assembleDebug
      # Create APK Release
      - name: Build apk release project (APK) - ${{ env.main_project_module }} module
        run: ./gradlew assemble
      # Create Bundle AAB Release
      # Noted for main module build [main_project_module]:bundleRelease
      - name: Build app bundle release (AAB) - ${{ env.main_project_module }} module
        run: ./gradlew ${{ env.main_project_module }}:bundleRelease
      # Upload Artifact Build
      # Noted For Output [main_project_module]/build/outputs/apk/debug/
      - name: Upload APK Debug - ${{ env.repository_name }}
        uses: actions/upload-artifact@v4
        with:
          name: ${{ env.date_today }} - ${{ env.playstore_name }} - ${{ env.repository_name }} - APK(s) debug generated
          path: ${{ env.main_project_module }}/build/outputs/apk/debug/
      # Noted For Output [main_project_module]/build/outputs/apk/release/
      - name: Upload APK Release - ${{ env.repository_name }}
        uses: actions/upload-artifact@v4
        with:
          name: ${{ env.date_today }} - ${{ env.playstore_name }} - ${{ env.repository_name }} - APK(s) release generated
          path: ${{ env.main_project_module }}/build/outputs/apk/release/
      # Noted For Output [main_project_module]/build/outputs/bundle/release/
      - name: Upload AAB (App Bundle) Release - ${{ env.repository_name }}
        uses: actions/upload-artifact@v4
        with:
          name: ${{ env.date_today }} - ${{ env.playstore_name }} - ${{ env.repository_name }} - App bundle(s) AAB release generated
          path: ${{ env.main_project_module }}/build/outputs/bundle/release/
      # ======================================================
      # Copy Build Outputs & Push to GitHub
      # ======================================================
      # Delete build/outputs directory if it already exists
      - name: Clean up build/outputs directory
        run: rm -rf ${{ env.build_output_path }}
      # Create build/outputs directory if it doesn't exist
      - name: Create build/outputs directory
        run: mkdir -p ${{ env.build_output_path }}
      # Copy APK Debug to build/outputs
      - name: Copy APK Debug to build/outputs
        run: |
          cp -r ${{ env.main_project_module }}/build/outputs/apk/debug/* ${{ env.build_output_path }}/ 2>/dev/null || echo "No APK debug files found"
      # Copy APK Release to build/outputs
      - name: Copy APK Release to build/outputs
        run: |
          cp -r ${{ env.main_project_module }}/build/outputs/apk/release/* ${{ env.build_output_path }}/ 2>/dev/null || echo "No APK release files found"
      # Copy AAB Release to build/outputs
      - name: Copy AAB Release to build/outputs
        run: |
          cp -r ${{ env.main_project_module }}/build/outputs/bundle/release/* ${{ env.build_output_path }}/ 2>/dev/null || echo "No AAB release files found"
      # List copied files for verification
      - name: List build/outputs contents
        run: ls -la ${{ env.build_output_path }}/
      # Commit and Push to GitHub
      - name: Commit & Push build outputs to GitHub
        run: |
          git config user.name '${{ github.actor }}'
          git config user.email '${{ github.actor }}@users.noreply.github.com'
          git add ${{ env.build_output_path }}/ -f
          git diff --cached --quiet && echo "No changes to commit" || (git commit -m "ci: upload build outputs - ${{ env.date_today }} [skip ci]" && git push)
```
- Project must be android studio project using gradle

- Create Files with name generate-apk-aab-debug-release.yml inside folder .github/workflows/
- .github/workflows/generate-apk-aab-debug-release.yml this is position files

```
name: Generated APK AAB (Upload - Create Artifact To Github Action)
env:
  # The name of the main module repository
  main_project_module: app
  # The name of the Play Store
  playstore_name: Frogobox ID
on:
  push:
    branches:
      - 'release/**'
  # Allows you to run this workflow manually from the Actions tab
  workflow_dispatch:
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      # Set Current Date As Env Variable
      - name: Set current date as env variable
        run: echo "date_today=$(date +'%Y-%m-%d')" >> $GITHUB_ENV
      # Set Repository Name As Env Variable
      - name: Set repository name as env variable
        run: echo "repository_name=$(echo '${{ github.repository }}' | awk -F '/' '{print $2}')" >> $GITHUB_ENV
      - name: Set Up JDK
        uses: actions/setup-java@v4
        with:
          distribution: 'zulu' # See 'Supported distributions' for available options
          java-version: '17'
          cache: 'gradle'
      - name: Change wrapper permissions
        run: chmod +x ./gradlew
      # Run Tests Build
      - name: Run gradle tests
        run: ./gradlew test
      # Run Build Project
      - name: Build gradle project
        run: ./gradlew build
      # Create APK Debug
      - name: Build apk debug project (APK) - ${{ env.main_project_module }} module
        run: ./gradlew assembleDebug
      # Create APK Release
      - name: Build apk release project (APK) - ${{ env.main_project_module }} module
        run: ./gradlew assemble
      # Create Bundle AAB Release
      # Noted for main module build [main_project_module]:bundleRelease
      - name: Build app bundle release (AAB) - ${{ env.main_project_module }} module
        run: ./gradlew ${{ env.main_project_module }}:bundleRelease
      # Upload Artifact Build
      # Noted For Output [main_project_module]/build/outputs/apk/debug/
      - name: Upload APK Debug - ${{ env.repository_name }}
        uses: actions/upload-artifact@v4
        with:
          name: ${{ env.date_today }} - ${{ env.playstore_name }} - ${{ env.repository_name }} - APK(s) debug generated
          path: ${{ env.main_project_module }}/build/outputs/apk/debug/
      # Noted For Output [main_project_module]/build/outputs/apk/release/
      - name: Upload APK Release - ${{ env.repository_name }}
        uses: actions/upload-artifact@v4
        with:
          name: ${{ env.date_today }} - ${{ env.playstore_name }} - ${{ env.repository_name }} - APK(s) release generated
          path: ${{ env.main_project_module }}/build/outputs/apk/release/
      # Noted For Output [main_project_module]/build/outputs/bundle/release/
      - name: Upload AAB (App Bundle) Release - ${{ env.repository_name }}
        uses: actions/upload-artifact@v4
        with:
          name: ${{ env.date_today }} - ${{ env.playstore_name }} - ${{ env.repository_name }} - App bundle(s) AAB release generated
          path: ${{ env.main_project_module }}/build/outputs/bundle/release/
```
```
name: Generated APK AAB (Clean)
on:
  # Allows you to run this workflow manually from the Actions tab
  workflow_dispatch:
  schedule:
    # Every day at 1am
    - cron: '0 1 * * *'
jobs:
  remove-old-artifacts:
    runs-on: ubuntu-latest
    timeout-minutes: 10
    steps:
      - name: Clean all artifacts
        uses: c-hive/gha-remove-artifacts@v4
        with:
          age: '60 seconds' # '<number> <unit>', e.g. 5 days, 2 years, 90 seconds, parsed by Moment.js
          # Optional inputs
          # skip-tags: true
          # skip-recent: 5
```
- Check Bundletool on (.github/lib/bundletool.jar) [Download Latest](https://github.com/google/bundletool/releases)

#### Step 2. Code Action in file [android-ci-generate-apk-aab-upload-3.yml](https://github.com/amirisback/automated-build-android-app-with-github-action/blob/master/.github/workflows/android-ci-generate-apk-aab-upload-3.yml)

```
name: Generated APK AAB 2 Bundle Tool (Upload - Create Artifact To Github Action)
env:
  # The name of the main module repository
  main_project_module: app
  # The name of the Play Store
  playstore_name: Frogobox ID
  # Keystore Path
  ks_path: frogoboxdev.jks
  # Keystore Password
  ks_store_pass: cronoclez
  # Keystore Alias
  ks_alias: frogobox
  # Keystore Alias Password
  ks_alias_pass: xeonranger
on:
  push:
    branches:
      - 'release/**'
  # Allows you to run this workflow manually from the Actions tab
  workflow_dispatch:
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      # Set Current Date As Env Variable
      - name: Set current date as env variable
        run: echo "date_today=$(date +'%Y-%m-%d')" >> $GITHUB_ENV
      # Set Repository Name As Env Variable
      - name: Set repository name as env variable
        run: echo "repository_name=$(echo '${{ github.repository }}' | awk -F '/' '{print $2}')" >> $GITHUB_ENV
      - name: Set Up JDK
        uses: actions/setup-java@v4
        with:
          distribution: 'zulu' # See 'Supported distributions' for available options
          java-version: '17'
          cache: 'gradle'
      - name: Change wrapper permissions
        run: chmod +x ./gradlew
      # Run Tests Build
      - name: Run gradle tests
        run: ./gradlew test
      # Run Build Project
      - name: Build gradle project
        run: ./gradlew build
      # Create APK Debug
      - name: Build apk debug project (APK) - ${{ env.main_project_module }} module
        run: ./gradlew assembleDebug
      # Create APK Release
      - name: Build apk release project (APK) - ${{ env.main_project_module }} module
        run: ./gradlew assemble
      # Create Bundle AAB Release
      # Noted for main module build [main_project_module]:bundleRelease
      - name: Build app bundle release (AAB) - ${{ env.main_project_module }} module
        run: ./gradlew ${{ env.main_project_module }}:bundleRelease
      # - name: Build APK(s) Debug from bundle using bundletool
      #   run: java -jar ".github/lib/bundletool.jar" build-apks --bundle=${{ env.main_project_module }}/build/outputs/bundle/debug/${{ env.artifact_name }}-debug.aab --output=${{ env.main_project_module }}/build/outputs/bundle/debug/${{ env.artifact_name }}-debug.apks --mode=universal
      - name: Set Env Artifact name from generated aab
        run: |
          cd ${{ env.main_project_module }}/build/outputs/bundle/release/
          files=(*)
          echo "generated_name_aab=${files[0]%.*}" >> $GITHUB_ENV
      # Build APK From Bundle Using Bundletool
      # Noted For Output [main_project_module]/build/outputs/bundle/release/
      - name: Build APK(s) Release from bundle using bundletool (Path same with bundle output)
        run: java -jar ".github/lib/bundletool.jar" build-apks --bundle=${{ env.main_project_module }}/build/outputs/bundle/release/${{ env.generated_name_aab }}.aab --output=${{ env.main_project_module }}/build/outputs/bundle/release/${{ env.generated_name_aab }}.apks --mode=universal --ks="app/${{ env.ks_path }}" --ks-pass=pass:${{ env.ks_store_pass }} --ks-key-alias=${{ env.ks_alias }} --key-pass=pass:${{ env.ks_alias_pass }}
      # Duplicate APK(s) Release to zip file and extract
      - name: Duplicate APK(s) Release to zip file and extract
        run: |
          cd ${{ env.main_project_module }}/build/outputs/bundle/release/
          unzip -p ${{ env.generated_name_aab }}.apks universal.apk > ${{ env.generated_name_aab }}.apk
      # Upload Artifact Build
      # Noted For Output [main_project_module]/build/outputs/apk/debug/
      - name: Upload APK Debug - ${{ env.repository_name }}
        uses: actions/upload-artifact@v4
        with:
          name: ${{ env.date_today }} - ${{ env.playstore_name }} - ${{ env.repository_name }} - APK(s) debug generated
          path: ${{ env.main_project_module }}/build/outputs/apk/debug/
      # Noted For Output [main_project_module]/build/outputs/apk/release/
      - name: Upload APK Release - ${{ env.repository_name }}
        uses: actions/upload-artifact@v4
        with:
          name: ${{ env.date_today }} - ${{ env.playstore_name }} - ${{ env.repository_name }} - APK(s) release generated
          path: ${{ env.main_project_module }}/build/outputs/apk/release/
      # Noted For Output [main_project_module]/build/outputs/bundle/release/
      - name: Upload AAB (App Bundle) Release - ${{ env.repository_name }}
        uses: actions/upload-artifact@v4
        with:
          name: ${{ env.date_today }} - ${{ env.playstore_name }} - ${{ env.repository_name }} - App bundle(s) AAB release generated
          path: ${{ env.main_project_module }}/build/outputs/bundle/release/
```
```
<component name="ProjectRunConfigurationManager">
  <!-- Add Name Configuration Here -->
  <configuration default="false" name="${your-config-name}" type="GradleRunConfiguration" factoryName="Gradle">
    <ExternalSystemSettings>
      <option name="executionName" />
      <option name="externalProjectPath" value="$PROJECT_DIR$" />
      <option name="externalSystemIdString" value="GRADLE" />
      <option name="scriptParameters" value="" />
      <option name="taskDescriptions">
        <list />
      </option>
      <option name="taskNames">
        <list>
          <!-- TODO : add your task here -->
          <option value=":app:assembleDebug" />
        </list>
      </option>
      <option name="vmOptions" />
    </ExternalSystemSettings>
    <ExternalSystemDebugServerProcess>true</ExternalSystemDebugServerProcess>
    <ExternalSystemReattachDebugProcess>true</ExternalSystemReattachDebugProcess>
    <DebugAllEnabled>false</DebugAllEnabled>
    <RunAsTest>false</RunAsTest>
    <method v="2" />
  </configuration>
</component>
```
```
<component name="ProjectRunConfigurationManager">
  <configuration default="false" name="signingreport" type="GradleRunConfiguration" factoryName="Gradle">
    <ExternalSystemSettings>
      <option name="executionName" />
      <option name="externalProjectPath" value="$PROJECT_DIR$" />
      <option name="externalSystemIdString" value="GRADLE" />
      <option name="scriptParameters" value="" />
      <option name="taskDescriptions">
        <list />
      </option>
      <option name="taskNames">
        <list>
          <option value="signingreport" />
        </list>
      </option>
      <option name="vmOptions" />
    </ExternalSystemSettings>
    <ExternalSystemDebugServerProcess>true</ExternalSystemDebugServerProcess>
    <ExternalSystemReattachDebugProcess>true</ExternalSystemReattachDebugProcess>
    <DebugAllEnabled>false</DebugAllEnabled>
    <RunAsTest>false</RunAsTest>
    <method v="2" />
  </configuration>
</component>
```
```
@echo off
setlocal
:: Navigate to the project root directory
cd /d "%~dp0.."
echo ======================================
    Starting Android Build Process    
echo ======================================
echo [1/6] Cleaning project...
call gradlew clean
echo [2/6] Running tests...
call gradlew test
echo [3/6] Building project...
call gradlew build
echo [4/6] Assembling Debug APK...
call gradlew assembleDebug
echo [5/6] Assembling Release APK...
call gradlew assemble
echo [6/6] Building Release App Bundle (AAB)...
call gradlew app:bundleRelease
echo ======================================
     Build completed successfully!    
echo ======================================
pause
```
```
#!/bin/bash
echo "======================================"
echo "     Starting Android Build Process    "
echo "======================================"
echo "[1/6] Cleaning project..."
./gradlew clean
echo "[2/6] Running tests..."
./gradlew test
echo "[3/6] Building project..."
./gradlew build
echo "[4/6] Assembling Debug APK..."
./gradlew assembleDebug
echo "[5/6] Assembling Release APK..."
./gradlew assemble
echo "[6/6] Building Release App Bundle (AAB)..."
./gradlew app:bundleRelease
echo "======================================"
echo "     Build completed successfully!    "
echo "======================================"
```
Very open to anyone, I'll write your name under this, please contribute by sending an email to me

- Mail To [faisalamircs@gmail.com](mailto:faisalamircs@gmail.com)
- Subject : Github _ [Github-Username-Account] _ [Language] _ [Repository-Name]
- Example : Github_amirisback_kotlin_admob-helper-implementation

Name Of Contribute

- Muhammad Faisal Amir
- Waiting List
- Waiting List

Waiting for your contribute

This project includes an **AI Agent Skill** designed to help AI coding assistants (like Antigravity) understand and manage the GitHub Workflows in this repository.

If you are using an AI assistant, you can ask it to use the skill located at:
`skills/github-workflows/SKILL.md`

- "Explain how the APK upload workflow works using the `github-workflows`skill."
- "Use the `github-workflows`skill to add a new environment variable to all CI scripts."
- "Help me troubleshoot a failed build using the `github-workflows`skill."

- Please enjoy and don't forget fork and give a star
- Don't Forget Follow My Github Account

## Resources

**automated-build-android-app-with-github-action** is not certified by GitHub. It is provided by a third-party and is governed by separate terms of service, privacy policy, and support documentation.