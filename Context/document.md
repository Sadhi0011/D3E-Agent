    **Hunk Format:**

    Each change hunk should represent a distinct set of modifications. The format is as follows:

    * **Newly Added Lines:**

        ```
        +New Line 1 of new addition (Markdown content)
        +New Line 2 of new addition (Markdown content)
        ```

    * **Changed Lines:**

        ```
         Unchanged line before the change (Markdown content)
         Unchanged line after the change (Markdown content)
        -Original line before modification (Markdown content)
        +Modified line after modification (Markdown content)
        +Newly added line (Markdown content)
        ```

    * **Removed Lines:**

        ```
         Unchanged line before removal (Markdown content)
        -Line to be removed (Markdown content)
         Unchanged line after removal (Markdown content)
        ```

    * **Additions within existing Lines:**

        ```
         Unchanged lines (Markdown content)
        -Original line (Markdown content)
        +Modified original line (Markdown content)
         Unchanged lines (Markdown content)
        +Newly added line (Markdown content)
        ```

    * **Additions at the beginning of a document:**

        ```
        +Newly added line at the start (Markdown content)
         Unchanged line 1 (Markdown content)
        ```

    * **Removals at the end of a document:**

        ```
         Unchanged line N (Markdown content)
        -Line removed at the end (Markdown content)
        ```

    **Important Guidelines:**

    1.  **Strict Format Adherence:** The output *must* follow the specified hunk format precisely.
    2.  **Markdown Content:** The content within each hunk line **must be valid Markdown**.
    3.  **No Headers:** Do not include any headers or metadata like file names or diff timestamps.
    4.  **Line Prefixes:** Use "+" to indicate added lines and "-" to indicate removed lines. Unchanged lines are displayed without prefixes.
    5.  **Hunk Separation:** Separate each individual hunk with a separator update_document call
    6.  **Context Lines:** Include unchanged lines surrounding the changes to provide context.
    7.  **Output only the hunks.** Do not output any additional text outside of the hunk format.
    8.  **Every output line in hunk should have '+' or '-' or ' ' for added, deleted, or unchanged lines. These are not part of markdown but git diff format.** Every line should have prefix.
    9.  **No Prefix** will be considered as error.
    10. **If no existing architecture document is provided, generate the entire document in hunk format.**
    11. **Do not provide any explanations or summaries outside of the hunk format.**
    12. **No Escape** There is no escape char in hunk format, since first char was reserved for it. And system won't look inside any other char in the line. So, `+\# Heading` is not correct. The correct one is `+# Heading`.
