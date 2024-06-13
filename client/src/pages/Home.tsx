import { Box, CssBaseline } from "@mui/material";
import PrimaryAppBar from "./template/PrimaryAppBar";
import PriamryDraw from "./template/PrimaryDraw";
import SecondaryDraw from "./template/SecondaryDraw";
import Main from "./template/Main";
import PopularChannels from "../components/PrimaryDraw/PopularChannels";



const Home = () => {
    return (
        <>
            <Box sx={{display: "flex" }}>
                <CssBaseline />
                <PrimaryAppBar />
                <PriamryDraw>
                    <PopularChannels />
                </PriamryDraw>
                <SecondaryDraw />
                <Main />
            </Box>
        </>
    );
}

export default Home;