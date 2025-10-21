# Pushing to GitHub

Your sapphire-event-spectra package is now a git repository and ready to push to GitHub!

## ✅ Local Repository Created

The local git repository has been initialized and the initial commit has been made:
- Commit: `f7cc9a6`
- Files: 14 files (1,767 lines of code)
- Branch: `master`

## 📤 Steps to Push to GitHub

### Option 1: Create New Repository on GitHub (Recommended)

1. **Go to GitHub and create a new repository:**
   - Visit: https://github.com/new
   - Repository name: `sapphire-event-spectra`
   - Description: "Python package for SAPPHIRE solar particle event spectra (Jiggens et al. 2018)"
   - Choose: **Public** (so others can use it)
   - **DO NOT** initialize with README, .gitignore, or license (we already have these)
   - Click "Create repository"

2. **Connect your local repository to GitHub:**
   ```bash
   cd /home/flei/OneDrive/WSL/maire-s-run/sapphire-event-spectra
   
   # Add the GitHub remote (replace YOUR_USERNAME with your GitHub username)
   git remote add origin https://github.com/YOUR_USERNAME/sapphire-event-spectra.git
   
   # Or if you prefer SSH:
   # git remote add origin git@github.com:YOUR_USERNAME/sapphire-event-spectra.git
   
   # Rename branch to main (optional, GitHub's new default)
   git branch -M main
   
   # Push to GitHub
   git push -u origin main
   ```

### Option 2: Push to ssc-maire Organization

If you want to add it to the ssc-maire organization:

1. **Create repository under ssc-maire:**
   - Visit: https://github.com/organizations/ssc-maire/repositories/new
   - Repository name: `sapphire-event-spectra`
   - Choose: **Public**
   - Click "Create repository"

2. **Connect and push:**
   ```bash
   cd /home/flei/OneDrive/WSL/maire-s-run/sapphire-event-spectra
   
   git remote add origin https://github.com/ssc-maire/sapphire-event-spectra.git
   git branch -M main
   git push -u origin main
   ```

## 📦 After Pushing to GitHub

Once pushed, users can install directly from GitHub:

```bash
# Install latest version
pip install git+https://github.com/YOUR_USERNAME/sapphire-event-spectra.git

# Or from ssc-maire organization
pip install git+https://github.com/ssc-maire/sapphire-event-spectra.git

# Install specific version/tag
pip install git+https://github.com/YOUR_USERNAME/sapphire-event-spectra.git@v1.0.0
```

## 🏷️ Creating a Release (Optional)

After pushing, you can create a release on GitHub:

1. Go to your repository on GitHub
2. Click "Releases" → "Create a new release"
3. Tag: `v1.0.0`
4. Title: "v1.0.0 - Initial Release"
5. Description: Add release notes
6. Click "Publish release"

## 📝 Adding Topics to Repository

After creating the repository on GitHub, add these topics to make it discoverable:
- `space-weather`
- `solar-particle-events`
- `sapphire`
- `radiation`
- `proton-spectra`
- `space-physics`
- `python`
- `scientific-computing`

## 🔄 Future Updates

When you make changes:

```bash
cd /home/flei/OneDrive/WSL/maire-s-run/sapphire-event-spectra

# Make your changes, then:
git add .
git commit -m "Description of changes"
git push
```

## 📊 Current Status

```
Repository: /home/flei/OneDrive/WSL/maire-s-run/sapphire-event-spectra
Status: ✅ Initialized and committed locally
Next: Push to GitHub (see instructions above)
```

## 🎉 Ready to Share!

Once pushed to GitHub, your package will be:
- ✅ Publicly accessible
- ✅ Installable via pip from GitHub
- ✅ Citable with a DOI (if you link to Zenodo)
- ✅ Discoverable by the space weather community
