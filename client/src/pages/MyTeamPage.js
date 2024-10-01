import React, { useEffect, useState } from 'react'; // Import necessary React features
import TeamAttendanceOverview from '../components/TeamAttendanceOverview'; // Import the attendance overview component
import TeamLeaveRequests from '../components/TeamLeaveRequests'; // Import the leave requests component

const MyTeamPage = () => {
    const [attendanceData, setAttendanceData] = useState([]); // State for attendance data
    const [leaveRequests, setLeaveRequests] = useState([]); // State for leave requests
    const [error, setError] = useState(null); // State for error handling

    useEffect(() => {
        const fetchAttendanceData = async () => {
            try {
                const response = await fetch('/api/manager/{manager_id}/team-attendance'); // Fetch attendance data
                if (!response.ok) throw new Error('Network response was not ok'); // Error handling for fetch
                const data = await response.json(); // Parse JSON response
                setAttendanceData(data); // Set attendance data into state
            } catch (error) {
                setError(error.message); // Set error message to state
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

    return (
        <main className="flex flex-col p-4"> {/* Main content styling */}
            {error ? ( // Conditional rendering for error
                <div role="alert" className="text-red-600">{error}</div> // Display error message
            ) : (
                <>
                    <TeamAttendanceOverview data={attendanceData} /> {/* Attendance overview component */}
                    <TeamLeaveRequests requests={leaveRequests} /> {/* Leave requests component with fetched leave requests */}
                </>
            )}
        </main>
    );
};

export default MyTeamPage; // Export the component for use in other parts of the application.