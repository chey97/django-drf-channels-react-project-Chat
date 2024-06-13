import { Box, CssBaseline } from "@mui/material";
import PrimaryAppBar from "./template/PrimaryAppBar";
import PriamryDraw from "./template/PrimaryDraw";
import SecondaryDraw from "./template/SecondaryDraw";
import Main from "./template/Main";
import PopularChannels from "../components/PrimaryDraw/PopularChannels";
import ExploreCategories from "../components/SecondaryDraw/ExploreCategories";



const Home = () => {
    return (
        <>
            <Box sx={{display: "flex" }}>
                <CssBaseline />
                <PrimaryAppBar />
                <PriamryDraw>
                    <PopularChannels open={false} />
                </PriamryDraw>
                <SecondaryDraw >
                    <ExploreCategories />
                </SecondaryDraw>
                <Main />
            </Box>
        </>
    );
}

export default Home;