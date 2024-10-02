import React, { useEffect, useState } from 'react'; // Import necessary React features
import TeamAttendanceOverview from '../components/TeamAttendanceOverview'; // Import the attendance overview component
import TeamLeaveRequests from '../components/TeamLeaveRequests'; // Import the leave requests component
import AttendanceReport from '../components/AttendanceReport'; // Import the attendance report component

const MyTeamPage = () => {
    const [attendanceData, setAttendanceData] = useState([]); // State for attendance data
    const [leaveRequests, setLeaveRequests] = useState([]); // State for leave requests
    const [error, setError] = useState(null); // State for error handling
    const [reportData, setReportData] = useState([]); // State for report data
    const [dateRange, setDateRange] = useState({ start_date: '', end_date: '' }); // State for date range

    useEffect(() => {
        const fetchAttendanceData = async () => {
            try {
                const response = await fetch('/api/manager/{manager_id}/team-attendance'); // Fetch attendance data
                if (!response.ok) throw new Error('Network response was not ok'); // Error handling for fetch
                const data = await response.json(); // Parse JSON response
                setAttendanceData(data); // Set attendance data into state
            } catch (error) {
                setError(error.message); // Set error message to state
                // Mock data in case of fetch failure
                setAttendanceData([{ employee: 'John Doe', attendance: 80 }, { employee: 'Jane Smith', attendance: 75 }]);
            }
        };

        const fetchLeaveRequests = async () => {
            try {
                const response = await fetch('/api/manager/{manager_id}/team-leave-requests'); // Fetch leave requests
                if (!response.ok) throw new Error('Network response was not ok'); // Error handling for fetch
                const data = await response.json(); // Parse JSON response
                setLeaveRequests(data); // Set leave requests into state
            } catch (error) {
                // Fallback to mock data if fetch fails
                setLeaveRequests([
                    { id: 1, employeeName: 'John Doe', startDate: '2023-10-01', endDate: '2023-10-05', status: 'Pending' },
                    { id: 2, employeeName: 'Jane Smith', startDate: '2023-10-10', endDate: '2023-10-12', status: 'Pending' },
                ]);
                setError(error.message); // Set error message to state
            }
        };

        fetchAttendanceData(); // Call the fetch function for attendance data
        fetchLeaveRequests(); // Call the fetch function for leave requests
    }, []); // Empty dependency array for componentDidMount behavior

    const handleDateChange = (e) => {
        setDateRange({ ...dateRange, [e.target.name]: e.target.value }); // Update date range
    };

    const generateReport = async () => {
        try {
            const response = await fetch(`/api/manager/{manager_id}/attendance-reports?start_date=${dateRange.start_date}&end_date=${dateRange.end_date}`); // Fetch report data
            if (!response.ok) throw new Error('Network response was not ok');
            const data = await response.json();
            setReportData(data); // Set report data into state
        } catch (error) {
            setError(error.message); // Set error message to state
            // Mock report data in case of fetch failure
            setReportData([{ date: '2023-10-01', present: 10, absent: 2 }, { date: '2023-10-02', present: 12, absent: 1 }]);
        }
    };

    return (
        <main className="flex flex-col p-4"> {/* Main content styling */}
         
                    <TeamAttendanceOverview data={attendanceData} /> {/* Attendance overview component */}
                    <TeamLeaveRequests requests={leaveRequests} /> {/* Leave requests component with fetched leave requests */}
                    <AttendanceReport 
                        dateRange={dateRange} 
                        onDateChange={handleDateChange} 
                        onGenerateReport={generateReport} 
                        reportData={reportData} 
                    /> {/* Attendance report component */}
        </main>
    );
};

export default MyTeamPage; // Export the component for use in other parts of the application