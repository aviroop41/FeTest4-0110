import React, { useEffect, useState } from 'react'; // Import necessary React libraries
import EmployeeDashboard from '../components/EmployeeDashboard'; // Import the EmployeeDashboard component

const DashboardPage = () => {
    const [attendanceData, setAttendanceData] = useState(null); // State for attendance data
    const [leaveBalance, setLeaveBalance] = useState(null); // State for leave balance
    const [recentActivities, setRecentActivities] = useState([]); // State for recent activities
    const [error, setError] = useState(null); // State for error handling

    // Fetch data from APIs
    const fetchData = async () => {
        try {
            const employeeId = 1; // Replace with actual employee ID
            const attendanceResponse = await fetch(`http://localhost:8080/api/employee/${employeeId}/attendance`);
            const leaveResponse = await fetch(`http://localhost:8080/api/employee/${employeeId}/leave-balance`);
            const activitiesResponse = await fetch(`http://localhost:8080/api/employee/${employeeId}/recent-activities`);

            if (!attendanceResponse.ok || !leaveResponse.ok || !activitiesResponse.ok) {
                throw new Error('Failed to fetch data');
            }

            const attendanceResult = await attendanceResponse.json();
            const leaveResult = await leaveResponse.json();
            const activitiesResult = await activitiesResponse.json();

            setAttendanceData(attendanceResult);
            setLeaveBalance(leaveResult);
            setRecentActivities(activitiesResult);
        } catch (err) {
            setError(err.message); // Set error message in case of failure
            // Mock data in case of error
            setAttendanceData({ total: 20, present: 18 }); // Example mock data
            setLeaveBalance({ total: 15, used: 5 }); // Example mock data
            setRecentActivities([{ id: 1, activity: 'Completed project A' }, { id: 2, activity: 'Attended training' }]); // Example mock data
        }
    };

    useEffect(() => {
        fetchData(); // Call fetch data function on component mount
    }, []);

    return (
        <div className="p-4 min-h-screen"> {/* Main content area */}
            {error && <div className="text-red-500">{error}</div>} {/* Display error if any */}
            <h1 className="text-2xl font-semibold mb-4">Dashboard</h1>
            <EmployeeDashboard 
                attendanceData={attendanceData} 
                leaveBalance={leaveBalance} 
                recentActivities={recentActivities} 
            /> {/* Render EmployeeDashboard with fetched data */}
        </div>
    );
};

export default DashboardPage; // Export DashboardPage for use in other components