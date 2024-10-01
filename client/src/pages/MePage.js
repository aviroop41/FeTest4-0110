import React, { useEffect, useState } from 'react';
import AttendanceDetails from '../components/AttendanceDetails'; // Importing the AttendanceDetails component
import LeaveRequestForm from '../components/LeaveRequestForm'; // Importing the LeaveRequestForm component

const MePage = () => {
    const [attendanceData, setAttendanceData] = useState([]); // State for attendance data
    const [loading, setLoading] = useState(true); // State for loading status
    const [error, setError] = useState(null); // State for potential errors
    const [leaveRequests, setLeaveRequests] = useState([]); // State to manage leave requests

    useEffect(() => {
        const fetchAttendanceDetails = async () => {
            try {
                const response = await fetch('http://localhost:8080/api/employee/1/attendance-details'); // Mocking employee_id
                if (!response.ok) {
                    throw new Error('Failed to fetch attendance details');
                }
                const data = await response.json(); 
                setAttendanceData(data);
            } catch (err) {
                setError(err.message); // Set error message if fetch fails; sample/mock data used for demonstration
                setAttendanceData([{ date: '2023-10-01', status: 'Present' }, { date: '2023-10-02', status: 'Absent' }]); // Mock data
            } finally {
                setLoading(false); // Set loading to false after fetch completion
            }
        };

        fetchAttendanceDetails(); // Call the fetch function
    }, []); // Empty dependency array to run only once on component mount

    const handleLeaveRequestSubmit = async (leaveData) => {
        try {
            const response = await fetch('http://localhost:8080/api/employee/1/request-leave', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(leaveData)
            });
            if (!response.ok) {
                throw new Error('Failed to submit leave request');
            }
            const newLeaveRequest = await response.json();
            setLeaveRequests([...leaveRequests, newLeaveRequest]); // Update leave requests with newly added leave
        } catch (err) {
            setError(err.message); // Set error message if submit fails
            alert("Leave request submission failed"); // Alert for the user in case of failure
        }
    };

    if (loading) return <div className="text-center">Loading...</div>; // Loading state

    if (error) return <div className="text-red-600">Error: {error}</div>; // Error handler

    return (
        <main className="p-4">
            <h1 className="text-2xl font-bold mb-4">My Attendance Records</h1>
            <AttendanceDetails data={attendanceData} /> {/* Passing attendance data to the AttendanceDetails component */}
            <LeaveRequestForm onSubmit={handleLeaveRequestSubmit} /> {/* Including LeaveRequestForm for leave requests */}
        </main>
    );
};

export default MePage; // Exporting MePage for use in App.js.