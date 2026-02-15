// Student Dashboard Logic

document.addEventListener('DOMContentLoaded', () => {
    // Check auth
    checkAuth();

    // Set user info
    const userName = localStorage.getItem('user_name') || 'Student';
    document.getElementById('user-name').textContent = userName;
    document.getElementById('user-avatar').textContent = userName.charAt(0).toUpperCase();

    // Set Date
    document.getElementById('current-date').textContent = new Date().toLocaleDateString();

    // Load Data
    console.log("Student Dashboard v5 Loaded");
    loadDashboardData();
});

async function loadDashboardData() {
    try {
        await Promise.all([
            fetchStats(),
            fetchDrives(),
            fetchHistory()
        ]);
    } catch (error) {
        console.error('Error loading dashboard:', error);
        showMessage('Failed to load some data', 'error');
    }
}

async function fetchStats() {
    try {
        const response = await fetch(`${API_BASE_URL}/student/dashboard-stats`);
        const data = await response.json();

        if (response.ok) {
            document.getElementById('stat-interviews').textContent = data.total_interviews || 0;
            document.getElementById('stat-avg-score').textContent = data.avg_score || '0.0';

            // Render Skill Heatmap
            const heatmapContainer = document.getElementById('skill-heatmap-container');
            if (data.skill_performance && data.skill_performance.length > 0) {
                heatmapContainer.innerHTML = '';
                data.skill_performance.forEach(skill => {
                    const score = skill.avg_score;
                    let color = '#e74c3c'; // red
                    if (score >= 8) color = '#2ecc71'; // green
                    else if (score >= 5) color = '#f1c40f'; // yellow

                    const width = (score / 10) * 100;

                    const item = document.createElement('div');
                    item.className = 'skill-item';
                    item.innerHTML = `
                        <div style="display: flex; justify-content: space-between; margin-bottom: 5px;">
                            <span style="font-weight: 600; color: var(--text-bright);">${skill.skill}</span>
                            <span style="color: ${color}; font-family: var(--font-code);">${score}/10</span>
                        </div>
                        <div style="width: 100%; background: rgba(255,255,255,0.1); border-radius: 4px; height: 8px; overflow: hidden;">
                            <div style="width: ${width}%; background: ${color}; height: 100%; border-radius: 4px; transition: width 1s ease;"></div>
                        </div>
                        <div style="font-size: 0.7rem; color: var(--text-dim); margin-top: 4px; text-align: right;">${skill.count} answers</div>
                    `;
                    heatmapContainer.appendChild(item);
                });
            }
        }
    } catch (e) {
        console.error('Stats error:', e);
    }
}

async function fetchDrives() {
    const list = document.getElementById('drives-list');
    try {
        const response = await fetch(`${API_BASE_URL}/student/drives`);
        const drives = await response.json();

        if (!response.ok) throw new Error(drives.error);

        list.innerHTML = '';
        if (drives.length === 0) {
            list.innerHTML = '<p style="color: var(--text-dim); text-align: center;">No upcoming drives found.</p>';
            return;
        }

        drives.forEach(drive => {
            const date = new Date(drive.date).toLocaleDateString();

            // Determine Match Color
            let matchColor = '#95a5a6'; // gray
            if (drive.match_score >= 70) matchColor = '#2ecc71'; // green
            else if (drive.match_score >= 40) matchColor = '#f1c40f'; // yellow
            else if (drive.match_score > 0) matchColor = '#e74c3c'; // red

            const card = document.createElement('div');
            card.className = 'drive-card';
            card.innerHTML = `
                <div class="drive-header">
                    <div>
                        <div class="company-name">${drive.company}</div>
                        <div class="role-name">${drive.role}</div>
                    </div>
                    <div style="text-align: right;">
                        <span class="status-badge status-${drive.status.toLowerCase()}">${drive.status}</span>
                        ${drive.match_score !== undefined ? `
                            <div style="margin-top: 5px; font-size: 0.8rem; font-weight: bold; color: ${matchColor}; border: 1px solid ${matchColor}; padding: 2px 6px; border-radius: 4px; display: inline-block;">
                                ${drive.match_score}% Match
                            </div>
                        ` : ''}
                    </div>
                </div>
                <div class="drive-meta">
                    <span>📅 ${date}</span>
                    ${drive.required_skills ? `<span title="${drive.required_skills}">🛠 Skills: ${drive.required_skills.substring(0, 30)}${drive.required_skills.length > 30 ? '...' : ''}</span>` : ''}
                </div>
                <p style="color: var(--text-dim); margin-bottom: 15px; font-size: 0.9rem;">
                    ${drive.description || 'No description available.'}
                </p>
                <a href="upload_resume.html" class="btn-apply" style="display: block; text-align: center; text-decoration: none;">Available - Prepare Now</a>
            `;
            list.appendChild(card);
        });

    } catch (e) {
        console.error('Drives error:', e);
        list.innerHTML = '<p style="color: red; text-align: center;">Error loading drives.</p>';
    }
}

async function fetchHistory() {
    const tbody = document.getElementById('history-table-body');
    try {
        const response = await fetch(`${API_BASE_URL}/student/history?t=${new Date().getTime()}`);
        const history = await response.json();
        console.log("History Data Received:", history);

        if (!response.ok) throw new Error(history.error);

        tbody.innerHTML = '';
        if (history.length === 0) {
            tbody.innerHTML = '<tr><td colspan="5" style="text-align: center;">No interview history.</td></tr>';
            return;
        }

        history.forEach(item => {
            const tr = document.createElement('tr');
            tr.innerHTML = `
                <td>${formatDate(item.started_at)}</td>
                <td><span class="status-badge status-${item.status === 'completed' ? 'completed' : 'upcoming'}">${item.status}</span></td>
                <td>${item.total_score ? item.total_score.toFixed(1) : '-'}</td>
                <td>${item.total_questions || '-'}</td>
            `;
            tbody.appendChild(tr);
        });

    } catch (e) {
        console.error('History error:', e);
        tbody.innerHTML = '<tr><td colspan="4" style="text-align: center; color: red;">Error loading history.</td></tr>';
    }
}

function viewReport(sessionId) {
    console.log("viewReport called with ID:", sessionId);
    if (!sessionId || sessionId === 'undefined' || sessionId === 'null') {
        alert('Error: Session ID is missing for this report. Check console for details.');
        return;
    }
    window.location.href = `result.html?session_id=${sessionId}`;
}

function showSection(sectionId, clickedLink) {
    if (clickedLink) {
        document.querySelectorAll('.nav-item').forEach(el => el.classList.remove('active'));
        clickedLink.classList.add('active');
    }

    document.querySelectorAll('.view-section').forEach(el => el.style.display = 'none');
    document.getElementById(`view-${sectionId}`).style.display = 'block';

    // Update header
    const titles = {
        'dashboard': 'Dashboard',
        'history': 'My Interview History'
    };
    document.getElementById('page-title').textContent = titles[sectionId] || 'Dashboard';
}
