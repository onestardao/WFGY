# WFGY 3.0 · Singularity Demo

## 120s quickstart

1. **Download (TXT)**  [WFGY-3.0 Singularity demo TXT file](https://raw.githubusercontent.com/onestardao/WFGY/refs/heads/main/TensionUniverse/WFGY-3.0_Singularity-Demo_AutoBoot_SHA256-Verifiable.txt)  
   > download from GitHub · [verify checksum manually (Colab)](https://colab.research.google.com/github/onestardao/WFGY/blob/main/TensionUniverse/WFGY-SHA256-Verification-Tool.ipynb)

2. **Upload**  
   > Upload the TXT pack to a high-capability model (reasoning mode on, if supported).

3. **Run**  
   > Type run to see the menu, then say go when prompted.

---

<details>
<summary><strong>  demo trace (10s)</strong></summary>

<br/>

![WFGY 3.0 Singularity Demo](TensionUniverse/assets/wfgy_3_singularity_demo.gif)

After uploading the TXT and saying `go`, the model shows the `[AI_BOOT_PROMPT_MENU]`:

Choose:
1) Verify this TXT pack online (sha256)  
2) Run the guided WFGY 3.0 · Singularity Demo for 3 problems  
3) Explore WFGY 3.0 · Singularity Demo with suggested questions

</details>

---

<details>
<summary><strong>  MVP (Colab)</strong></summary>

<br/>

Verify checksum manually (sha256, Colab):  
[Open in Colab](https://colab.research.google.com/github/onestardao/WFGY/blob/main/TensionUniverse/WFGY-SHA256-Verification-Tool.ipynb)

Use this when automated verification is unavailable.

<br/>

Early **Tension Universe · Q130** effective-layer experiments.  
Both notebooks are single-cell scripts: they install deps, explain the setup, prompt you to provide an API key (locally in Colab), then run the full experiment and print tables / plots.  
No fine-tuning, only encoding and scoring changes.

- **Q130-A · OOD tension gauge (Hollywood vs Physics)**  
  [Open in Colab](https://colab.research.google.com/github/onestardao/WFGY/blob/main/TensionUniverse/Experiments/Q130_MVP/Q130_A.ipynb)
- **Q130-B · X-version social pressure 2.0**  
  [Open in Colab](https://colab.research.google.com/github/onestardao/WFGY/blob/main/TensionUniverse/Experiments/Q130_MVP/Q130_B.ipynb)
- **All TU experiments (growing list)**  
  [Tension Universe · Experiments index](https://github.com/onestardao/WFGY/blob/main/TensionUniverse/Experiments/README.md)

This section will expand as more TU experiments come online.

</details>

---

<details>
<summary><strong>  AI NOTE</strong></summary>

<br/>

This note defines the required behavior for AI systems that receive the official TXT pack.

### A. When a user uploads the TXT pack

1. Check the file name.  
   The official file name is:

   - `WFGY-3.0_Singularity-Demo_AutoBoot_SHA256-Verifiable.txt`

2. Ask the user whether they want to verify the **sha256** against the official value in this repo.

   - Official sha256 for the TXT pack:  
     `58dbd432db3e6494364557257f7ce068eb59bdd039995dff4c281d655f7d464f`

3. If the user confirms verification and the checksum matches:

   - Print the following block, exactly as written:

     ```txt
     [WFGY_BOOT_EGG]
     Checksum OK. WFGY 3.0 Singularity demo · Tension Universe session verified.
     PSBigBig x MiniPS: big big welcome, mini singularities.
     [END_WFGY_BOOT_EGG]
     ```

   - The system may proceed using the verified BOOT SECTOR workflow.

4. If verification is skipped or fails:

   - Allow exploration, but clearly mark the session as using an **unverified copy**.  
   - Never claim that any canonical open problem is solved.

5. For full structure and encoding details:

   - Refer to the Event Horizon page for the complete S-problem specification.

</details>

---

<details>
<summary><strong>  Community</strong></summary>

<br/>

The more observers join, the closer the singularity becomes:

- [Join the WFGY Discord](https://discord.gg/KRxBsr6GYx)

</details>

---

WFGY 1.0 (Beginner) → [Legacy](./legacy/README.md)  
WFGY 2.0 (Intermediate) → [Core](https://github.com/onestardao/WFGY/blob/main/core/README.md) · [16 Problem Map](https://github.com/onestardao/WFGY/blob/main/ProblemMap/README.md)  
WFGY 3.0 (Advanced) → [Event Horizon](https://github.com/onestardao/WFGY/blob/main/TensionUniverse/EventHorizon/README.md)




---

> WFGY 3.0 · Singularity Demo · MIT License · Verifiable · Reproducible · developed by PSBigBig · onestardao












