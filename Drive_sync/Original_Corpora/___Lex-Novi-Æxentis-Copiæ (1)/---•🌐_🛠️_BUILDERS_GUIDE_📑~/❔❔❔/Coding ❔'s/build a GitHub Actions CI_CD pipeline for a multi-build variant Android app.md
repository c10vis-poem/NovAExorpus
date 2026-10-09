---
title: "build a GitHub Actions CI_CD pipeline for a multi-build variant Android app"
source: "Drive_sync/Original_Corpora/___Lex-Novi-Æxentis-Copiæ (1)/---•🌐_🛠️_BUILDERS_GUIDE_📑~/❔❔❔/Coding ❔'s/build a GitHub Actions CI_CD pipeline for a multi-build variant Android app.pdf"
cleaned: 2026-10-08
converter: "pymupdf get_text via tools/clean.py normalize_markdown"
tags:
  - pdf-conversion
---

In this video, we build a GitHub Actions CI/CD pipeline for a multi-build variant Android app.

.github/workflows/android-release-build.yml

https://x.com/anilvdes...
Official WebSite: https://codetutorhub.dev/

GitHub link to code: https://github.com/Ani

Original file line number​
Diff line number​
Diff line change
@@ -0,0 +1,129 @@
# ── Android CI — Scalable Secret Strategy ─────────────────────────────
# This workflow lives on `main` (so GitHub discovers it in the Actions tab)
# but checks out whichever branch you specify in the inputs.
#
# Secret injection follows the same classification as build.gradle.kts:
#   COMMON            → ANALYTICS_SDK_KEY (always injected)
#   ENVIRONMENT-SPECIFIC → BACKEND_TOKEN_<ENV> (all three, always)
#   TIER-SPECIFIC     → AD_SDK_KEY_<TIER> (both, always)
#   RELEASE-ONLY      → RELEASE_SIGNING_* (only when buildType=release)
#
# ⚠️  IMPORTANT: Gradle evaluates ALL productFlavors at configuration time,
#     so all common/env/tier secrets must be present for every build.
#     Only signing secrets are truly conditional (use resolveSecretOrNull).
#
# No giant if-else. The variant name encodes the env, tier, and buildType.

name: Android Manual Variant Build

on:
  workflow_dispatch:
    inputs:
      branch:
        description: 'Branch to build from'
        required: true
        type: string
        default: 'live-coding'
      variant:
        description: 'Variant to build'
        required: true
        type: choice
        options:
          - qaFreeDebug
          - qaPaidDebug


          - stagingFreeDebug
          - stagingPaidDebug
          - prodFreeRelease
          - prodPaidRelease

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v5
        with:
          ref: ${{ inputs.branch }}

      - name: Derive env, tier, and buildType from variant name
        id: classify
        run: |
          VARIANT="${{ inputs.variant }}"
          echo "variant=$VARIANT"

          # Extract environment (first segment: qa, staging, or prod)
          if [[ "$VARIANT" == qa* ]]; then
            ENV="QA"
          elif [[ "$VARIANT" == staging* ]]; then
            ENV="STAGING"
          elif [[ "$VARIANT" == prod* ]]; then
            ENV="PROD"
          fi

          # Extract tier (middle segment: Free or Paid)
          if [[ "$VARIANT" == *Free* ]]; then
            TIER="FREE"
          elif [[ "$VARIANT" == *Paid* ]]; then
            TIER="PAID"
          fi

          # Extract build type (last segment: Debug or Release)
          if [[ "$VARIANT" == *Debug ]]; then
            BUILD_TYPE="debug"
          elif [[ "$VARIANT" == *Release ]]; then
            BUILD_TYPE="release"
          fi

          {


            echo "env=$ENV"
            echo "tier=$TIER"
            echo "buildType=$BUILD_TYPE"
          } >> "$GITHUB_OUTPUT"

          echo "── Classification ──"
          echo "  Environment : $ENV"
          echo "  Tier        : $TIER"
          echo "  Build Type  : $BUILD_TYPE"
      - name: Set up JDK 21
        uses: actions/setup-java@v5
        with:
          distribution: temurin
          java-version: '21'

      - name: Build variant
        env:
          # ── COMMON (always) ──────────────────────────────────────
          ANALYTICS_SDK_KEY: ${{ secrets.ANALYTICS_SDK_KEY }}

          # ── ENVIRONMENT-SPECIFIC (all three — Gradle configures ──
          # every flavor at configuration time, regardless of which
          # variant you're building)
          BACKEND_TOKEN_QA: ${{ secrets.BACKEND_TOKEN_QA }}
          BACKEND_TOKEN_STAGING: ${{ secrets.BACKEND_TOKEN_STAGING }}
          BACKEND_TOKEN_PROD: ${{ secrets.BACKEND_TOKEN_PROD }}

          # ── TIER-SPECIFIC (both — same reason as above) ──────────
          AD_SDK_KEY_FREE: ${{ secrets.AD_SDK_KEY_FREE }}
          AD_SDK_KEY_PAID: ${{ secrets.AD_SDK_KEY_PAID }}

          # ── RELEASE-ONLY (signing — only when buildType=release) ─
          # These are the one category that IS truly conditional:
          # signingConfigs uses resolveSecretOrNull, so empty is OK.
          RELEASE_SIGNING_STORE_FILE:     ${{ steps.classify.outputs.buildType == 'release'
&& secrets.RELEASE_SIGNING_STORE_FILE     || '' }}
          RELEASE_SIGNING_STORE_PASSWORD: ${{ steps.classify.outputs.buildType ==
'release' && secrets.RELEASE_SIGNING_STORE_PASSWORD || '' }}
          RELEASE_SIGNING_KEY_ALIAS:      ${{ steps.classify.outputs.buildType == 'release' &&
secrets.RELEASE_SIGNING_KEY_ALIAS      || '' }}
          RELEASE_SIGNING_KEY_PASSWORD:   ${{ steps.classify.outputs.buildType ==
'release' && secrets.RELEASE_SIGNING_KEY_PASSWORD   || '' }}
        run: |
          chmod +x ./gradlew


          VARIANT="${{ inputs.variant }}"
          TASK_NAME="assemble${VARIANT^}"
          echo "Building: ./gradlew $TASK_NAME"
          echo "  Secrets injected for: env=${{ steps.classify.outputs.env }}, tier=${{
steps.classify.outputs.tier }}, buildType=${{ steps.classify.outputs.buildType }}"
          ./gradlew "$TASK_NAME"
      - name: Upload APK
        uses: actions/upload-artifact@v5
        with:
          name: ${{ inputs.variant }}-apk
          path: app/build/outputs/apk/**/*.apk

github/workflows/android-main-build.yml

github/workflows/android-pr-checks.yml  and

.github/workflows/android-release-build.yml


-0,0 +1,56 @@
name: Android Release Build

on:
  workflow_dispatch:
    inputs:
      variant:
        description: 'Release variant to build'
        required: true
        type: choice
        options:
          - prodFreeRelease
          - prodPaidRelease

permissions:
  contents: read

jobs:
  signed-release:
    name: Trusted release build
    runs-on: ubuntu-latest
    environment: production

    steps:
      - name: Checkout code


        uses: actions/checkout@v5

      - name: Set up JDK 21
        uses: actions/setup-java@v5
        with:
          distribution: temurin
          java-version: '21'

      - name: Build signed release variant
        env:
          ANALYTICS_SDK_KEY: ${{ secrets.ANALYTICS_SDK_KEY }}
          BACKEND_TOKEN_QA: ${{ secrets.BACKEND_TOKEN_QA }}
          BACKEND_TOKEN_STAGING: ${{ secrets.BACKEND_TOKEN_STAGING }}
          BACKEND_TOKEN_PROD: ${{ secrets.BACKEND_TOKEN_PROD }}
          AD_SDK_KEY_FREE: ${{ secrets.AD_SDK_KEY_FREE }}
          AD_SDK_KEY_PAID: ${{ secrets.AD_SDK_KEY_PAID }}
          RELEASE_SIGNING_STORE_FILE: ${{ secrets.RELEASE_SIGNING_STORE_FILE }}
          RELEASE_SIGNING_STORE_PASSWORD: ${{
secrets.RELEASE_SIGNING_STORE_PASSWORD }}
          RELEASE_SIGNING_KEY_ALIAS: ${{ secrets.RELEASE_SIGNING_KEY_ALIAS }}
          RELEASE_SIGNING_KEY_PASSWORD: ${{
secrets.RELEASE_SIGNING_KEY_PASSWORD }}
        run: |
          chmod +x ./gradlew
          VARIANT="${{ inputs.variant }}"
          TASK_NAME="assemble${VARIANT^}"
          echo "Building trusted release artifact: ./gradlew $TASK_NAME"
          ./gradlew "$TASK_NAME"
      - name: Upload signed release APK
        uses: actions/upload-artifact@v5
        with:
          name: ${{ inputs.variant }}-signed-apk
          path: app/build/outputs/apk/**/*.apk
