#!/bin/bash
# Script to set up GitHub remote and push the repository

echo "=================================================="
echo "SAPPHIRE Event Spectra - GitHub Push Helper"
echo "=================================================="
echo ""

# Check if we're in the right directory
if [ ! -d ".git" ]; then
    echo "❌ Error: Not in a git repository. Please run from sapphire-event-spectra directory."
    exit 1
fi

echo "This script will help you push the repository to GitHub."
echo ""
echo "First, create a new repository on GitHub:"
echo "  1. Go to https://github.com/new"
echo "  2. Repository name: sapphire-event-spectra"
echo "  3. Make it Public"
echo "  4. DO NOT initialize with README, .gitignore, or license"
echo "  5. Click 'Create repository'"
echo ""
read -p "Have you created the repository on GitHub? (y/n): " created

if [ "$created" != "y" ] && [ "$created" != "Y" ]; then
    echo "Please create the repository first, then run this script again."
    exit 0
fi

echo ""
echo "Choose repository owner:"
echo "1) Personal account (https://github.com/YOUR_USERNAME/sapphire-event-spectra)"
echo "2) ssc-maire organization (https://github.com/ssc-maire/sapphire-event-spectra)"
echo "3) Custom URL"
echo ""
read -p "Enter choice [1-3]: " owner_choice

case $owner_choice in
    1)
        read -p "Enter your GitHub username: " username
        remote_url="https://github.com/${username}/sapphire-event-spectra.git"
        ;;
    2)
        remote_url="https://github.com/ssc-maire/sapphire-event-spectra.git"
        ;;
    3)
        read -p "Enter full GitHub repository URL: " remote_url
        ;;
    *)
        echo "❌ Invalid choice"
        exit 1
        ;;
esac

echo ""
echo "Repository URL: $remote_url"
echo ""
read -p "Is this correct? (y/n): " confirm

if [ "$confirm" != "y" ] && [ "$confirm" != "Y" ]; then
    echo "Aborted."
    exit 0
fi

echo ""
echo "Setting up remote..."

# Check if remote already exists
if git remote get-url origin &> /dev/null; then
    echo "Remote 'origin' already exists. Removing..."
    git remote remove origin
fi

# Add new remote
git remote add origin "$remote_url"
echo "✅ Remote added: $remote_url"

# Rename branch to main (GitHub's default)
echo ""
echo "Renaming branch to 'main'..."
git branch -M main
echo "✅ Branch renamed to 'main'"

# Push to GitHub
echo ""
echo "Pushing to GitHub..."
git push -u origin main

if [ $? -eq 0 ]; then
    echo ""
    echo "=================================================="
    echo "✅ SUCCESS! Repository pushed to GitHub!"
    echo "=================================================="
    echo ""
    echo "Your repository is now available at:"
    echo "${remote_url%.git}"
    echo ""
    echo "Users can install it with:"
    echo "pip install git+${remote_url}"
    echo ""
    echo "Next steps:"
    echo "  1. Add repository description and topics on GitHub"
    echo "  2. Create a release (v1.0.0) for easier referencing"
    echo "  3. Add badges to README (optional)"
    echo ""
else
    echo ""
    echo "❌ Push failed. Possible reasons:"
    echo "  - Repository doesn't exist on GitHub"
    echo "  - Authentication issues (may need to set up SSH key or personal access token)"
    echo "  - Network connectivity issues"
    echo ""
    echo "To push manually:"
    echo "  git push -u origin main"
fi
