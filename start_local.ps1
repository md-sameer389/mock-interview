
Write-Host "Stopping existing Python processes..."
Get-Process python -ErrorAction SilentlyContinue | Stop-Process -Force

Write-Host "Starting Backend Server..."
Start-Process python -ArgumentList "backend/app.py" -WindowStyle Normal

Start-Sleep -Seconds 2

Write-Host "Starting Frontend Server..."
Start-Process python -ArgumentList "run_frontend.py" -WindowStyle Normal

Write-Host "Local Environment Started!"
Write-Host "Backend: http://127.0.0.1:5000"
Write-Host "Frontend: http://localhost:8000"
Write-Host "Opening Admin Dashboard..."
Start-Process "http://localhost:8000/admin.html"
