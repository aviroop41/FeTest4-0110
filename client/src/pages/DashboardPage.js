import React, { useEffect, useState } from 'react'; // Import necessary React libraries
import EmployeeDashboard from '../components/EmployeeDashboard'; // Import the EmployeeDashboard component
import Notifications from '../components/Notifications'; // Import the Notifications component

const DashboardPage = () => {
    const [attendanceData, setAttendanceData] = useState(null); // State for attendance data
    const [leaveBalance, setLeaveBalance] = useState(null); // State for leave balance
    const [recentActivities, setRecentActivities] = useState([]); // State for recent activities
    const [notifications, setNotifications] = useState([]); // State for notifications
    const [error, setError] = useState(null); // State for error handling

    // Fetch data from APIs
    const fetchData = async () => {
        try {
            const employeeId = 1; // Replace with actual employee ID
            const attendanceResponse = await fetch(`http://localhost:8080/api/employee/${employeeId}/attendance`);
            const leaveResponse = await fetch(`http://localhost:8080/api/employee/${employeeId}/leave-balance`);
            const activitiesResponse = await fetch(`http://localhost:8080/api/employee/${employeeId}/recent-activities`);
            const notificationsResponse = await fetch(`http://localhost:8080/api/employee/${employeeId}/notifications`);

            if (!attendanceResponse.ok || !leaveResponse.ok || !activitiesResponse.ok || !notificationsResponse.ok) {
                throw new Error('Failed to fetch data');
            }

            const attendanceResult = await attendanceResponse.json();
            const leaveResult = await leaveResponse.json();
            const activitiesResult = await activitiesResponse.json();
            const notificationsResult = await notificationsResponse.json();

            setAttendanceData(attendanceResult);
            setLeaveBalance(leaveResult);
            setRecentActivities(activitiesResult);
            setNotifications(notificationsResult);
        } catch (err) {
            setError(err.message); // Set error message in case of failure
            // Mock data in case of error
            setAttendanceData({ total: 20, present: 18 }); // Example mock data
            setLeaveBalance({ total: 15, used: 5 }); // Example mock data
            setRecentActivities([
                { id: 1, activity: 'Completed project A' },
                { id: 2, activity: 'Attended training' },
                { id: 3, activity: 'Participated in team meeting' }, // New mock data
                { id: 4, activity: 'Submitted performance review' } // New mock data
            ]); // Example mock data
            setNotifications([
                { id: 1, message: 'Leave request approved', status: 'unread' },
                { id: 2, message: 'Leave request denied', status: 'unread' },
                { id: 3, message: 'New policy update available', status: 'unread' }, // New mock notification
                { id: 4, message: 'Meeting scheduled for next week', status: 'unread' } // New mock notification
            ]); // Example mock notifications
        }
    };

    // Mark notification as read
    const markNotificationAsRead = async (notificationId) => {
        try {
            const employeeId = 1; // Replace with actual employee ID
            await fetch(`http://localhost:8080/api/employee/${employeeId}/notifications/${notificationId}/read`, {
                method: 'POST',
            });
            setNotifications(notifications.map(notification => 
                notification.id === notificationId ? { ...notification, status: 'read' } : notification
            ));
        } catch (err) {
            setError(err.message); // Handle error if the mark as read fails
        }
    };

    useEffect(() => {
        fetchData(); // Call fetch data function on component mount
    }, []);

    return (
        <div className="p-4 min-h-screen"> {/* Main content area */}
            <h1 className="text-2xl font-semibold mb-4">Dashboard</h1>
            <EmployeeDashboard 
                attendanceData={attendanceData} 
                leaveBalance={leaveBalance} 
                recentActivities={recentActivities} 
            /> {/* Render EmployeeDashboard with fetched data */}
            <Notifications notifications={notifications} onMarkAsRead={markNotificationAsRead} /> {/* Render Notifications component */}
        </div>
    );
};

export default DashboardPage; // Export DashboardPage for use in other components.