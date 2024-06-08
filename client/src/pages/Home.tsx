import { Box, CssBaseline } from "@mui/material";
import PrimaryAppBar from "./template/PrimaryAppBar";
import PriamryDraw from "./template/PrimaryDraw";
import SecondaryDraw from "./template/SecondaryDraw";



const Home = () => {
    return (
        <>
            <Box sx={{display: "flex" }}>
                <CssBaseline />
                <PrimaryAppBar />
                <PriamryDraw />
                <SecondaryDraw />
            </Box>
        </>
    );
}

export default Home;