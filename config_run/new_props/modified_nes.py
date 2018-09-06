import lsst.pex.config as pexConfig
from lsst.ts.schedulerConfig.proposal import General, SelectionList, TimeRange
from lsst.ts.schedulerConfig.proposal import GeneralBandFilter, Selection
from lsst.ts.schedulerConfig.proposal import general_prop_reg
__all__ = ["ModNorthEclipticSpur"]
@pexConfig.registerConfig("ModNorthEclipticSpur", general_prop_reg, General)
class ModNorthEclipticSpur(General):
    def setDefaults(self):
        General.setDefaults(self)
        self.name = "ModNorthEclipticSpur"
        # -------------------------
        # Sky Region specifications
        # -------------------------
        sel0 = Selection()
        sel0.limit_type = "EB"
        sel0.minimum_limit = -30.0
        sel0.maximum_limit = 10.0
        sel1 = Selection()
        sel1.limit_type = "Dec"
        sel1.minimum_limit = 2.8
        sel1.maximum_limit = 90.0
        self.sky_region.selections = {0: sel0,
                                      1: sel1}
        time_range0 = TimeRange()
        time_range0.start = 1
        time_range0.end = 1460
        time_range1 = TimeRange()
        time_range1.start = 1
        time_range1.end = 1460
        self.sky_region.time_ranges = {0: time_range0,
                                       1: time_range1}
        sel_map0 = SelectionList()
        sel_map0.indexes = [0, 1]
        self.sky_region.selection_mapping = {0: sel_map0}
        # ----------------------------
        # Sky Exclusion specifications
        # ----------------------------
        self.sky_exclusion.dec_window = 90.0
        # ---------------------------------
        # Sky Nightly Bounds specifications
        # ---------------------------------
        self.sky_nightly_bounds.twilight_boundary = -12.0
        self.sky_nightly_bounds.delta_lst = 60.0
        # ------------------------------
        # Sky Constraints specifications
        # ------------------------------
        self.sky_constraints.max_airmass = 2.5
        self.sky_constraints.max_cloud = 0.7
        self.sky_constraints.min_distance_moon = 30.0
        self.sky_constraints.exclude_planets = True
        # ----------------------
        # Scheduling information
        # ----------------------
        self.scheduling.max_num_targets = 100
        self.scheduling.accept_serendipity = False
        self.scheduling.accept_consecutive_visits = False
        self.scheduling.airmass_bonus = 0.0
        self.scheduling.hour_angle_bonus = 0.3
        self.scheduling.hour_angle_max = 3.0
        self.scheduling.restrict_grouped_visits = True
        self.scheduling.time_interval = 1800.0
        self.scheduling.time_window_start = 0.5
        self.scheduling.time_window_max = 1.0
        self.scheduling.time_window_end = 2.0
        self.scheduling.time_weight = 1.0
        # --------------------------
        # Band Filter specifications
        # --------------------------
        g_filter = GeneralBandFilter()
        g_filter.name = 'g'
        g_filter.num_visits = 20
        g_filter.num_grouped_visits = 2
        g_filter.bright_limit = 21.0
        g_filter.dark_limit = 30.0
        g_filter.max_seeing = 2.0
        g_filter.exposures = [15.0, 15.0]
        r_filter = GeneralBandFilter()
        r_filter.name = 'r'
        r_filter.num_visits = 46
        r_filter.num_grouped_visits = 2
        r_filter.bright_limit = 20.25
        r_filter.dark_limit = 30.0
        r_filter.max_seeing = 2.0
        r_filter.exposures = [15.0, 15.0]
        i_filter = GeneralBandFilter()
        i_filter.name = 'i'
        i_filter.num_visits = 46
        i_filter.num_grouped_visits = 2
        i_filter.bright_limit = 19.5
        i_filter.dark_limit = 30.0
        i_filter.max_seeing = 2.0
        i_filter.exposures = [15.0, 15.0]
        z_filter = GeneralBandFilter()
        z_filter.name = 'z'
        z_filter.num_visits = 40
        z_filter.num_grouped_visits = 2
        z_filter.bright_limit = 17.0
        z_filter.dark_limit = 21.0
        z_filter.max_seeing = 2.0
        z_filter.exposures = [15.0, 15.0]
        self.filters = {g_filter.name: g_filter,
                        r_filter.name: r_filter,
                        i_filter.name: i_filter,
                        z_filter.name: z_filter}
