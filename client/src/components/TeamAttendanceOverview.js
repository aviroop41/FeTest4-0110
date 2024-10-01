import React, { useEffect, useState } from 'react';

// Component to display attendance statistics for the team
const TeamAttendanceOverview = ({ managerId }) => {
    const [attendanceData, setAttendanceData] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    // Fetch attendance data from API
    useEffect(() => {
        const fetchAttendanceData = async () => {
            try {
                const response = await fetch(`http://localhost:8080/api/manager/${managerId}/team-attendance`);
                if (!response.ok) throw new Error('Failed to fetch attendance data');
                const data = await response.json();
                setAttendanceData(data);
            } catch (error) {
                setError(error.message);
            } finally {
                setLoading(false);
            }
        };

        fetchAttendanceData();
    }, [managerId]);

    // Placeholder mock data in case of API failure
    const mockData = [
        { name: "Alice", attendance: 95 },
        { name: "Bob", attendance: 85 },
        { name: "Charlie", attendance: 90 },
        { name: "David", attendance: 70 },
    ];

    const dataToDisplay = attendanceData.length ? attendanceData : mockData;

    return (
        <div className="p-4 bg-white rounded-lg shadow-md">
            <h2 className="text-xl font-semibold mb-4">Team Attendance Overview</h2>
            {loading && <p>Loading...</p>}
            {error && <p className="text-red-600">{error}</p>}
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
                {dataToDisplay.map((member) => (
                    <div key={member.name} className="bg-gray-100 p-4 rounded-md shadow-sm flex flex-col">
                        <h3 className="font-bold">{member.name}</h3>
                        <p className="text-lg">{member.attendance}% Attendance</p>
                    </div>
                ))}
            </div>
        </div>
    );
};

export default TeamAttendanceOverview;