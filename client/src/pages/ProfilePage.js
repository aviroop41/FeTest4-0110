import React, { useEffect, useState } from 'react';
import ProfileManagement from '../components/ProfileManagement';

const ProfilePage = () => {
    const [profileData, setProfileData] = useState(null);
    const [error, setError] = useState(null);

    useEffect(() => {
        const fetchProfileData = async () => {
            try {
                const response = await fetch('http://localhost:8080/api/employee/1/profile');
                if (!response.ok) {
                    throw new Error('Failed to fetch profile data');
                }
                const data = await response.json();
                setProfileData(data);
            } catch (err) {
                // Mock data in case of fetch failure
                setProfileData({
                    name: 'John Doe',
                    email: 'john.doe@example.com',
                    contact_number: '123-456-7890',
                    address: '123 Main St, Anytown, USA',
                });
                setError(err.message);
            }
        };

        fetchProfileData();
    }, []);

    return (
        <div className="p-4">
            <h1 className="text-2xl font-bold mb-4">Profile Management</h1>
            {error && <p className="text-red-500">{error}</p>}
            {profileData ? (
                <ProfileManagement profile={profileData} />
            ) : (
                <p>Loading...</p>
            )}
        </div>
    );
};

export default ProfilePage;