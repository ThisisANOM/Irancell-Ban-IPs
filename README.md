این کد Python برای مسدود کردن رنج‌های آی‌پی در سرور اوبونتو از طریق دستورات `iptables` استفاده می‌کند. این کد به شما این امکان را می‌دهد که رنج‌های آی‌پی مختلف را که در یک فایل قرار دارند، خط به خط بخواند و سپس این رنج‌ها را به `iptables` اضافه کند تا دسترسی از آنها به سرور مسدود شود.

### نحوه استفاده:

1. **آماده‌سازی فایل**: قبل از هر چیز، فایلی را که شامل رنج‌های آی‌پی می‌باشد (مثلاً با پسوند `.txt`) ایجاد یا آماده کنید و رنج‌های آی‌پی مورد نظر خود را در آن قرار دهید. هر خط از فایل باید یک رنج آی‌پی باشد.

2. **ویرایش کد Python**: مسیر و نام فایل مربوط به رنج‌های آی‌پی خود را در کد Python قرار دهید. این مسیر را در متغیر `file_path` قرار دهید.

3. **اجرای کد**: پس از آماده‌سازی، این کد Python را اجرا کنید. این کد به طور خودکار رنج‌های آی‌پی را از فایل مورد نظر خواهد خواند و سپس دستورات `iptables` را برای مسدود کردن آنها اجرا خواهد کرد.

### نحوه عملکرد:

1. **خواندن رنج‌های آی‌پی**: کد با استفاده از دستور `open` یک فایل را باز می‌کند و تمام رنج‌های آی‌پی موجود در آن فایل را خط به خط می‌خواند.

2. **پاکسازی داده‌ها**: رنج‌های آی‌پی خوانده شده را از فضای سفید و خطوط خالی پاکسازی می‌کند تا همه رنج‌ها صحیحاً تفسیر شوند.

3. **اعمال دستورات `iptables`**: برای هر یک از رنج‌های آی‌پی، از دستور `subprocess.run` استفاده می‌کند تا دستورات `iptables` را برای مسدود کردن این رنج‌ها به سرور اجرا کند. دستورات `iptables` از `-s` (source) استفاده می‌کنند تا منبع داده را تعیین کنند و با `-j DROP`، دستور مسدود سازی را اعمال می‌کنند.

4. **پایان اجرا**: پس از اتمام اعمال دستورات `iptables` برای تمام رنج‌های آی‌پی، اجرای کد به پایان می‌رسد و دسترسی به این رنج‌های آی‌پی به سرور مسدود می‌شود.

با اجرای این کد، دسترسی به رنج‌های آی‌پی مورد نظر شما به سرور مسدود می‌شود، اما توجه داشته باشید که این کار غیرقابل برگشت است و ممکن است برای دسترسی به سرور نیاز به تنظیمات دیگری داشته باشید. همچنین، اجرای کد نیاز به دسترسی sudo و یا اجازه اجرای دستورات iptables دارد.

This Python code is designed to block IP ranges on an Ubuntu server using `iptables` commands. It allows you to read various IP ranges line by line from a file and subsequently add these ranges to `iptables` to block access from those IPs to the server.

### How to Use:

1. **Prepare the File**: Create or prepare a file containing IP ranges (e.g., with a `.txt` extension) and place your desired IP ranges inside it. Each line of the file should represent an IP range.

2. **Edit the Python Code**: Set the path and name of the file containing your IP ranges within the Python code. Replace the file path in the `file_path` variable.

3. **Run the Code**: After preparing, execute this Python code. It will automatically read IP ranges from the specified file and then execute `iptables` commands to block those IPs.

### Functionality:

1. **Reading IP Ranges**: The code uses the `open` command to open a file and reads all the IP ranges line by line.

2. **Data Cleaning**: It cleans the read IP ranges from whitespace and empty lines to ensure accurate interpretation.

3. **Applying `iptables` Commands**: For each IP range, it utilizes `subprocess.run` to execute `iptables` commands, blocking these ranges from accessing the server. The `iptables` commands use `-s` (source) to specify the source data and `-j DROP` to implement the blocking action.

4. **Execution Completion**: Once it finishes applying `iptables` commands for all IP ranges, the code execution concludes, resulting in the blocked access of these specified IP ranges to the server.

By running this code, access to the specified IP ranges will be blocked from the server. Keep in mind that this action is irreversible and might require additional settings for server access. Additionally, executing the code needs sudo access or permission to run `iptables` commands.
