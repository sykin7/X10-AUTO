# x10hosting 自动保号脚本使用说明

为了让 GitHub Actions 能成功登录你的 x10hosting 账号，你需要手动添加两个 Repository Secrets（仓库机密变量）。

### 操作步骤（只需做一次）

1. 打开你的这个 GitHub 仓库页面  
2. 点击右上角的 **Settings（设置）**  
3. 在左侧边栏找到 **Secrets and variables** → 点击展开 → 选择 **Actions**  
4. 点击右上角绿色的 **New repository secret** 按钮  

#### 需要添加的两个 Secret：

**第一个**  
- **Name**：`XSRF_TOKEN`  
- **Secret**：打开 x10hosting 官网，登录你的账号后按 F12 → Network → Application → Cookies 中找到 `XSRF-TOKEN` 的值，整串复制（不含引号）  
  → 点击 **Add secret**

**第二个**  
- **Name**：`X10_SESSION`  
- **Secret**：同上，在 Cookies 中找到 `x10hosting_session` 的值，整串复制（不含引号）  
  → 点击 **Add secret**

> 两个都添加完成后页面会显示刚刚添加的两个变量名。

### 验证是否配置成功（手动跑一次即可）

1. 点击仓库上方的 **Actions** 标签  
2. 左侧工作流列表里找到 **x10hosting Auto KeepAlive**，点击它  
3. 右侧会出现一个蓝色的 **Run workflow** 按钮，点击  
4. 再点绿色的 **Run workflow** 确认运行  

等待 10~30 秒，刷新页面：  
- 如果工作流前面出现绿色的 ✔ 勾勾，表示成功  
- 点击进去查看日志，最后几行看到下面这行就彻底搞定啦：>>> 登录保号成功！，就说明搞定了！以后它每天都会自动跑
