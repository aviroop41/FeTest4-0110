import React, { useEffect, useState } from 'react';

const AttendanceDetails = ({ employeeId }) => {
    const [attendanceData, setAttendanceData] = useState([]);
    const [error, setError] = useState(null);

    const fetchAttendanceDetails = async () => {
        try {
            const response = await fetch(`http://localhost:8080/api/employee/${employeeId}/attendance-details`);
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            const data = await response.json();
            setAttendanceData(data);
        } catch (err) {
            setError('Failed to fetch attendance details. Showing mock data instead.');
            // Mock data in case of fetch failure
            setAttendanceData([
                { date: '2023-10-01', checkIn: '09:00 AM', checkOut: '05:00 PM', totalHours: 8 },
                { date: '2023-10-02', checkIn: '09:15 AM', checkOut: '05:15 PM', totalHours: 8 },
                { date: '2023-10-03', checkIn: '08:50 AM', checkOut: '04:50 PM', totalHours: 8 },
            ]);
        }
    };

    useEffect(() => {
        fetchAttendanceDetails();
    }, [employeeId]);

    return (
        <div className="overflow-x-auto">
            {error && <div className="text-red-500">{error}</div>}
            <table className="min-w-full bg-white border border-gray-200">
                <thead className="bg-gray-100">
                    <tr>
                        <th className="py-3 px-4 text-left text-gray-600">Date</th>
                        <th className="py-3 px-4 text-left text-gray-600">Check In</th>
                        <th className="py-3 px-4 text-left text-gray-600">Check Out</th>
                        <th className="py-3 px-4 text-left text-gray-600">Total Hours</th>
                    </tr>
                </thead>
                <tbody>
                    {attendanceData.map((record, index) => (
                        <tr key={index} className="hover:bg-gray-50">
                            <td className="py-3 px-4 border-b border-gray-200">{record.date}</td>
                            <td className="py-3 px-4 border-b border-gray-200">{record.checkIn}</td>
                            <td className="py-3 px-4 border-b border-gray-200">{record.checkOut}</td>
                            <td className="py-3 px-4 border-b border-gray-200">{record.totalHours}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
};

export default AttendanceDetails;