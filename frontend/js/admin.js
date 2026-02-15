const ADMIN_API_BASE = '/api/admin';

document.addEventListener('DOMContentLoaded', () => {
    // Ensure Auth
    if (typeof checkAuth === 'function') {
        checkAuth();
    }

    // Set Date
    document.getElementById('current-date').innerText = new Date().toLocaleDateString();

    // Load Data based on current view
    refreshCurrentView();
});

// Navigation State
let currentView = 'view-dashboard';

function navigateTo(viewId, navElement) {
    // 1. Update UI Tabs
    if (navElement) {
        document.querySelectorAll('.nav-item').forEach(el => el.classList.remove('active'));
        navElement.classList.add('active');
    }

    // 2. Switch Section
    document.querySelectorAll('.view-section').forEach(el => el.style.display = 'none');
    document.getElementById(viewId).style.display = 'block';

    currentView = viewId;

    // 3. Load Data
    refreshCurrentView();
}

function refreshCurrentView() {
    if (currentView === 'view-dashboard') {
        loadStats();
        loadActivity();
    } else if (currentView === 'view-students') {
        loadStudents();
    } else if (currentView === 'view-analytics') {
        loadAnalytics();
    } else if (currentView === 'view-drives') {
        loadDrives();
    } else if (currentView === 'view-reports') {
        loadReports();
    } else if (currentView === 'view-settings') {
        // No data load needed for now
    }
}

async function handleSystemReset() {
    if (!confirm("CRITICAL WARNING: This will delete ALL student interview data. Are you absolutely sure?")) return;

    // Double confirmation
    const verification = prompt("Type 'DELETE' to confirm:");
    if (verification !== 'DELETE') {
        alert("Reset cancelled.");
        return;
    }

    try {
        const response = await fetch(`${ADMIN_API_BASE}/reset`, { method: 'POST' });
        if (response.ok) {
            alert("System reset successful. All data cleared.");
            navigateTo('view-dashboard'); // Go back to dashboard to see empty stats
        } else {
            alert("Failed to reset system.");
        }
    } catch (e) {
        console.error(e);
        alert("Error resetting system");
    }
}

async function loadDrives() {
    const list = document.getElementById('drives-list');
    list.innerHTML = '<p>Loading drives...</p>';

    try {
        const response = await fetch(`${ADMIN_API_BASE}/drives`);
        const drives = await response.json();

        list.innerHTML = '';
        if (drives.length === 0) {
            list.innerHTML = '<p>No upcoming drives found.</p>';
            return;
        }

        drives.forEach(d => {
            const statusColor = d.status === 'Open' ? '#4cd137' : '#fbc531';
            const card = `
                <div class="drive-card">
                    <div style="display:flex; justify-content:space-between; align-items:start;">
                        <div>
                            <div class="drive-company">${d.company}</div>
                            <div class="drive-role">${d.role}</div>
                        </div>
                        <button class="btn-refresh" style="padding: 4px 8px; font-size: 0.8rem; background: rgba(255,0,0,0.1); color: #ff4757; border-color: #ff4757;" onclick="deleteDrive(${d.id})">Del</button>
                    </div>
                    <p style="font-size: 0.9rem; color: #ccc;">${d.description}</p>
                    <div class="drive-meta">
                        <span>📅 ${new Date(d.date).toLocaleDateString()}</span>
                        <span class="status-badge" style="color: ${statusColor}">${d.status}</span>
                    </div>
                </div>
            `;
            list.innerHTML += card;
        });
    } catch (e) {
        console.error(e);
        list.innerHTML = '<p style="color:red">Error loading drives: ' + e.message + '</p>';
        // alert("Error loading drives: " + e.message); // Temporary debug
    }
}

async function deleteDrive(id) {
    if (!confirm("Are you sure you want to delete this drive?")) return;

    try {
        const response = await fetch(`${ADMIN_API_BASE}/drives/${id}`, { method: 'DELETE' });
        if (response.ok) {
            loadDrives(); // Refresh list
        } else {
            alert("Failed to delete drive");
        }
    } catch (e) {
        console.error(e);
        alert("Error deleting drive");
    }
}

function openDriveModal() {
    document.getElementById('drive-modal').style.display = 'flex';
}

function closeDriveModal() {
    document.getElementById('drive-modal').style.display = 'none';
}

async function handleCreateDrive(e) {
    e.preventDefault();

    const data = {
        company: document.getElementById('drive-company').value,
        role: document.getElementById('drive-role').value,
        required_skills: document.getElementById('drive-skills').value,
        date: document.getElementById('drive-date').value,
        description: document.getElementById('drive-desc').value
    };

    try {
        const response = await fetch(`${ADMIN_API_BASE}/drives`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data)
        });

        if (response.ok) {
            closeDriveModal();
            document.getElementById('create-drive-form').reset();
            loadDrives(); // Refresh list
        } else {
            alert("Failed to create drive");
        }
    } catch (e) {
        console.error(e);
        alert("Error creating drive");
    }
}

// Chart Instances
let skillChart = null;
let activityChart = null;

async function loadAnalytics() {
    try {
        if (typeof Chart === 'undefined') {
            console.error("Chart.js not loaded");
            document.getElementById('chart-skills').parentNode.innerHTML = '<p style="color:red; text-align:center; padding: 20px;">Chart.js failed to load. Please check internet connection.</p>';
            return;
        }

        // 1. Skill Performance
        const skillRes = await fetch(`${ADMIN_API_BASE}/analytics/skills`);
        const skillData = await skillRes.json();

        const ctxSkills = document.getElementById('chart-skills').getContext('2d');
        if (skillChart) skillChart.destroy(); // Destroy old chart to avoid overlay

        skillChart = new Chart(ctxSkills, {
            type: 'bar',
            data: {
                labels: skillData.map(d => d.skill_name),
                datasets: [{
                    label: 'Avg Score (0-10)',
                    data: skillData.map(d => d.avg_score),
                    backgroundColor: 'rgba(108, 93, 211, 0.6)',
                    borderColor: 'rgba(108, 93, 211, 1)',
                    borderWidth: 1
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                scales: {
                    y: { beginAtZero: true, max: 10, grid: { color: 'rgba(255,255,255,0.1)' } },
                    x: { grid: { display: false } }
                },
                plugins: { legend: { display: false } }
            }
        });

        // 2. Activity
        const actRes = await fetch(`${ADMIN_API_BASE}/analytics/activity`);
        const actData = await actRes.json();

        const ctxAct = document.getElementById('chart-activity').getContext('2d');
        if (activityChart) activityChart.destroy();

        activityChart = new Chart(ctxAct, {
            type: 'line',
            data: {
                labels: actData.map(d => new Date(d.interview_date).toLocaleDateString()),
                datasets: [{
                    label: 'Interviews Conducted',
                    data: actData.map(d => d.session_count),
                    borderColor: '#00D2FF',
                    tension: 0.4,
                    pointBackgroundColor: '#00D2FF'
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                scales: {
                    y: { beginAtZero: true, grid: { color: 'rgba(255,255,255,0.1)' } },
                    x: { grid: { color: 'rgba(255,255,255,0.1)' } }
                }
            }
        });

    } catch (e) {
        console.error("Analytics Error:", e);
        // alert("Analytics Error: " + e.message); // Temporary debug
    }
}

async function loadStudents() {

    const tableBody = document.getElementById('students-table-body');
    if (!tableBody) {
        console.error("students-table-body not found!");
        return;
    }
    tableBody.innerHTML = '<tr><td colspan="6" style="text-align: center;">Loading students...</td></tr>';

    try {


        const response = await fetch(`${ADMIN_API_BASE}/students`);
        if (!response.ok) throw new Error("Failed to fetch students. Status: " + response.status);

        const data = await response.json();

        tableBody.innerHTML = '';
        if (data.length === 0) {
            tableBody.innerHTML = '<tr><td colspan="6">No students found</td></tr>';
            return;
        }

        data.forEach(s => {
            const row = `
                <tr>
                    <td><b>${s.full_name}</b></td>
                    <td>${s.email}</td>
                    <td>${s.total_sessions}</td>
                    <td>${s.avg_score}</td>
                    <td>${s.last_active ? new Date(s.last_active).toLocaleDateString() : '-'}</td>
                    <td><button class="btn-refresh" style="padding: 4px 8px; font-size: 0.8rem;" onclick="viewStudent(${s.id})">Details</button></td>
                </tr>
            `;
            tableBody.innerHTML += row;
        });

    } catch (e) {
        console.error("Error in loadStudents:", e);
        tableBody.innerHTML = '<tr><td colspan="6" style="color:red">Error loading students: ' + e.message + '</td></tr>';
    }
}

async function viewStudent(id) {
    const modal = document.getElementById('student-modal');
    modal.style.display = 'flex';

    // Clear previous data
    document.getElementById('modal-student-name').innerText = "Loading...";
    document.getElementById('modal-student-email').innerText = "";
    document.getElementById('modal-history-body').innerHTML = '<tr><td colspan="3" style="text-align:center">Loading history...</td></tr>';

    try {
        const response = await fetch(`${ADMIN_API_BASE}/students/${id}`);
        if (!response.ok) throw new Error("Failed to fetch student details. Status: " + response.status);

        const data = await response.json();

        if (data.error) {
            alert("Error: " + data.error);
            return;
        }

        document.getElementById('modal-student-name').innerText = data.user.full_name;
        document.getElementById('modal-student-email').innerText = data.user.email;

        const historyBody = document.getElementById('modal-history-body');
        historyBody.innerHTML = '';

        if (!data.sessions || data.sessions.length === 0) {
            historyBody.innerHTML = '<tr><td colspan="4" style="text-align:center">No interview history found.</td></tr>';
            return;
        }

        data.sessions.forEach(s => {
            const row = `
                <tr>
                    <td>${new Date(s.started_at).toLocaleDateString()}</td>
                    <td>${s.total_score ? s.total_score.toFixed(1) : '-'}</td>
                    <td>${s.status}</td>
                    <td>
                        <span style="color:var(--text-dim);">-</span>
                    </td>
                </tr>
            `;
            historyBody.innerHTML += row;
        });

    } catch (e) {
        console.error("Error in viewStudent:", e);
        document.getElementById('modal-history-body').innerHTML = `<tr><td colspan="4" style="color:red">Error: ${e.message}</td></tr>`;
    }
}

function closeModal() {
    document.getElementById('student-modal').style.display = 'none';
}

let currentReports = [];

async function loadReports() {
    const tableBody = document.getElementById('reports-table-body');
    tableBody.innerHTML = '<tr><td colspan="4" style="text-align: center;">Loading reports...</td></tr>';

    try {
        const response = await fetch(`${ADMIN_API_BASE}/reports`);
        if (!response.ok) throw new Error("Failed to fetch reports");
        const data = await response.json();
        currentReports = data; // Store for modal access

        tableBody.innerHTML = '';
        if (data.length === 0) {
            tableBody.innerHTML = '<tr><td colspan="4">No reported issues found.</td></tr>';
            return;
        }

        data.forEach((r, index) => {
            const row = `
                <tr>
                    <td>
                        <div style="font-weight: 600;">${r.student_name}</div>
                        <div style="font-size: 0.8rem; color: var(--text-dim);">ID: ${r.session_id}</div>
                    </td>
                    <td>
                        <div style="font-size: 0.9rem;">${r.question_text.substring(0, 50)}...</div>
                    </td>
                    <td>
                        <div style="color: #ff6b6b; font-weight:500;">${r.flag_reason.substring(0, 30)}${r.flag_reason.length > 30 ? '...' : ''}</div>
                    </td>
                    <td>
                        <button class="btn-refresh" onclick="openReportModal(${index})" style="padding: 4px 8px; font-size: 0.8rem;">View Details</button>
                    </td>
                </tr>
            `;
            tableBody.innerHTML += row;
        });

    } catch (e) {
        console.error("Error loading reports:", e);
        tableBody.innerHTML = '<tr><td colspan="4" style="color:red">Error loading reports</td></tr>';
    }
}

function openReportModal(index) {
    const r = currentReports[index];
    if (!r) return;

    const modalBody = document.getElementById('report-modal-body');
    modalBody.innerHTML = `
        <div style="margin-bottom: 15px;">
            <div style="font-size: 0.8rem; color: var(--text-dim);">Student</div>
            <div style="font-size: 1.1rem; font-weight: bold;">${r.student_name}</div>
        </div>
        <div style="margin-bottom: 15px;">
            <div style="font-size: 0.8rem; color: var(--text-dim);">Report Reason</div>
            <div style="color: #ff6b6b; font-weight: 500; font-size: 1.1rem; background: rgba(255, 107, 107, 0.1); padding: 10px; border-radius: 8px; white-space: pre-wrap; word-wrap: break-word;">${r.flag_reason}</div>
        </div>
        <div style="margin-bottom: 15px;">
            <div style="font-size: 0.8rem; color: var(--text-dim);">Question</div>
            <div>${r.question_text}</div>
        </div>
        <div style="margin-bottom: 15px;">
            <div style="font-size: 0.8rem; color: var(--text-dim);">User Answer</div>
            <div style="background: rgba(255,255,255,0.05); padding: 10px; border-radius: 8px;">${r.user_answer}</div>
        </div>
        <div style="margin-bottom: 15px;">
            <div style="font-size: 0.8rem; color: var(--text-dim);">AI Feedback</div>
            <div style="font-size: 0.9rem;">${r.feedback}</div>
        </div>
        <div style="margin-bottom: 15px;">
            <div style="font-size: 0.8rem; color: var(--text-dim);">Score</div>
            <div style="font-weight: bold; color: var(--secondary);">${r.score}/10</div>
        </div>
    `;

    document.getElementById('report-modal').style.display = 'flex';
}

function closeReportModal() {
    document.getElementById('report-modal').style.display = 'none';
}

async function loadStats() {
    try {
        const response = await fetch(`${ADMIN_API_BASE}/stats`);
        if (!response.ok) throw new Error("Failed to fetch stats");

        const data = await response.json();

        // Animate Numbers
        animateValue("stat-candidates", 0, data.total_candidates, 1000);
        animateValue("stat-interviews", 0, data.total_interviews, 1000);
        // Safe check for elements, as they might be hidden in some views? 
        // Actually stat cards are part of dashboard view, so they exist in DOM always, just hidden.
        document.getElementById('stat-avg-score').innerText = data.avg_score;
        document.getElementById('stat-readiness').innerText = data.placement_readiness + "%";

    } catch (e) {
        console.error("Stats Error:", e);
    }
}

async function loadActivity() {
    const tableBody = document.getElementById('activity-table-body');

    try {
        const response = await fetch(`${ADMIN_API_BASE}/activity`);
        if (!response.ok) throw new Error("Failed to fetch activity: " + response.status);

        const data = await response.json();

        tableBody.innerHTML = '';

        if (data.length === 0) {
            tableBody.innerHTML = '<tr><td colspan="5" style="text-align: center;">No recent activity</td></tr>';
            return;
        }

        data.forEach(item => {
            if (!item.started_at) { console.warn("Missing date", item); }
            const date = item.started_at ? new Date(item.started_at).toLocaleDateString() : 'N/A';
            const statusClass = item.status === 'completed' ? 'status-completed' : 'status-inprogress';
            const statusLabel = item.status === 'completed' ? 'Completed' : 'In Progress';

            const row = `
                <tr>
                    <td>
                        <div style="font-weight: 600;">${item.full_name || 'Unknown'}</div>
                        <div style="font-size: 0.8rem; color: #8b8fb1;">ID: ${item.session_id}</div>
                    </td>
                    <td>${date}</td>
                    <td><span class="${statusClass}">${statusLabel}</span></td>
                    <td>${item.questions_answered}</td>
                    <td>${item.total_score ? item.total_score.toFixed(1) : '-'}</td>
                </tr>
            `;
            tableBody.innerHTML += row;
        });

    } catch (e) {
        console.error("Activity Error:", e);
        tableBody.innerHTML = `<tr><td colspan="5" style="text-align: center; color: var(--error);">Error loading data: ${e.message}</td></tr>`;
    }
}

// Utility: Number Animation
function animateValue(id, start, end, duration) {
    if (start === end) return;
    const range = end - start;
    const obj = document.getElementById(id);
    let current = start;
    const increment = end > start ? 1 : -1;
    const stepTime = Math.abs(Math.floor(duration / range));

    const timer = setInterval(function () {
        current += increment;
        obj.innerHTML = current;
        if (current == end) {
            clearInterval(timer);
        }
    }, stepTime);
}
