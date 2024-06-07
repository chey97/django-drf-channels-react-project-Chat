import { Box, CssBaseline, useTheme } from "@mui/material";
import PrimaryAppBar from "./template/PrimaryAppBar";



const Home = () => {
    return (
        <>
            <Box sx={{display: "flex" }}>
                <CssBaseline />
                <PrimaryAppBar />
            </Box>
        </>
    );
}

export default Home;