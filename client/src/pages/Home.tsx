import { Box, CssBaseline } from "@mui/material";
import PrimaryAppBar from "./template/PrimaryAppBar";
import PriamryDraw from "./template/PrimaryDraw";
import SecondaryDraw from "./template/SecondaryDraw";
import Main from "./template/Main";



const Home = () => {
    return (
        <>
            <Box sx={{display: "flex" }}>
                <CssBaseline />
                <PrimaryAppBar />
                <PriamryDraw />
                <SecondaryDraw />
                <Main />
            </Box>
        </>
    );
}

export default Home;