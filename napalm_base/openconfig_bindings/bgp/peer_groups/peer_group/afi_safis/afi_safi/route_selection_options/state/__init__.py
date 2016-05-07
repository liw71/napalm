
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
class state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-bgp - based on the path /bgp/peer-groups/peer-group/afi-safis/afi-safi/route-selection-options/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: State information for the route selection options
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__always_compare_med','__ignore_as_path_length','__external_compare_router_id','__advertise_inactive_routes','__enable_aigp','__ignore_next_hop_igp_metric',)

  _yang_name = 'state'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    helper = kwargs.pop("path_helper", None)
    if helper is False:
      self._path_helper = False
    elif helper is not None and isinstance(helper, xpathhelper.YANGPathHelper):
      self._path_helper = helper
    elif hasattr(self, "_parent"):
      helper = getattr(self._parent, "_path_helper", False)
      self._path_helper = helper
    else:
      self._path_helper = False

    self._extmethods = False
    self.__enable_aigp = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="enable-aigp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='boolean', is_config=False)
    self.__ignore_next_hop_igp_metric = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="ignore-next-hop-igp-metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='boolean', is_config=False)
    self.__always_compare_med = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="always-compare-med", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='boolean', is_config=False)
    self.__external_compare_router_id = YANGDynClass(base=YANGBool, default=YANGBool("true"), is_leaf=True, yang_name="external-compare-router-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='boolean', is_config=False)
    self.__ignore_as_path_length = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="ignore-as-path-length", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='boolean', is_config=False)
    self.__advertise_inactive_routes = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="advertise-inactive-routes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='boolean', is_config=False)

    load = kwargs.pop("load", None)
    if args:
      if len(args) > 1:
        raise TypeError("cannot create a YANG container with >1 argument")
      all_attr = True
      for e in self._pyangbind_elements:
        if not hasattr(args[0], e):
          all_attr = False
          break
      if not all_attr:
        raise ValueError("Supplied object did not have the correct attributes")
      for e in self._pyangbind_elements:
        nobj = getattr(args[0], e)
        if nobj._changed() is False:
          continue
        setmethod = getattr(self, "_set_%s" % e)
        if load is None:
          setmethod(getattr(args[0], e))
        else:
          setmethod(getattr(args[0], e), load=load)

  def _path(self):
    if hasattr(self, "_parent"):
      return self._parent._path()+[self._yang_name]
    else:
      return [u'bgp', u'peer-groups', u'peer-group', u'afi-safis', u'afi-safi', u'route-selection-options', u'state']

  def _get_always_compare_med(self):
    """
    Getter method for always_compare_med, mapped from YANG variable /bgp/peer_groups/peer_group/afi_safis/afi_safi/route_selection_options/state/always_compare_med (boolean)

    YANG Description: Compare multi-exit discriminator (MED) value from
different ASes when selecting the best route.  The
default behavior is to only compare MEDs for paths
received from the same AS.
    """
    return self.__always_compare_med
      
  def _set_always_compare_med(self, v, load=False):
    """
    Setter method for always_compare_med, mapped from YANG variable /bgp/peer_groups/peer_group/afi_safis/afi_safi/route_selection_options/state/always_compare_med (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_always_compare_med is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_always_compare_med() directly.

    YANG Description: Compare multi-exit discriminator (MED) value from
different ASes when selecting the best route.  The
default behavior is to only compare MEDs for paths
received from the same AS.
    """
    try:
      t = YANGDynClass(v,base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="always-compare-med", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='boolean', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """always_compare_med must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="always-compare-med", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='boolean', is_config=False)""",
        })

    self.__always_compare_med = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_always_compare_med(self):
    self.__always_compare_med = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="always-compare-med", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='boolean', is_config=False)


  def _get_ignore_as_path_length(self):
    """
    Getter method for ignore_as_path_length, mapped from YANG variable /bgp/peer_groups/peer_group/afi_safis/afi_safi/route_selection_options/state/ignore_as_path_length (boolean)

    YANG Description: Ignore the AS path length when selecting the best path.
The default is to use the AS path length and prefer paths
with shorter length.
    """
    return self.__ignore_as_path_length
      
  def _set_ignore_as_path_length(self, v, load=False):
    """
    Setter method for ignore_as_path_length, mapped from YANG variable /bgp/peer_groups/peer_group/afi_safis/afi_safi/route_selection_options/state/ignore_as_path_length (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ignore_as_path_length is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ignore_as_path_length() directly.

    YANG Description: Ignore the AS path length when selecting the best path.
The default is to use the AS path length and prefer paths
with shorter length.
    """
    try:
      t = YANGDynClass(v,base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="ignore-as-path-length", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='boolean', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ignore_as_path_length must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="ignore-as-path-length", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='boolean', is_config=False)""",
        })

    self.__ignore_as_path_length = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ignore_as_path_length(self):
    self.__ignore_as_path_length = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="ignore-as-path-length", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='boolean', is_config=False)


  def _get_external_compare_router_id(self):
    """
    Getter method for external_compare_router_id, mapped from YANG variable /bgp/peer_groups/peer_group/afi_safis/afi_safi/route_selection_options/state/external_compare_router_id (boolean)

    YANG Description: When comparing similar routes received from external
BGP peers, use the router-id as a criterion to select
the active path.
    """
    return self.__external_compare_router_id
      
  def _set_external_compare_router_id(self, v, load=False):
    """
    Setter method for external_compare_router_id, mapped from YANG variable /bgp/peer_groups/peer_group/afi_safis/afi_safi/route_selection_options/state/external_compare_router_id (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_external_compare_router_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_external_compare_router_id() directly.

    YANG Description: When comparing similar routes received from external
BGP peers, use the router-id as a criterion to select
the active path.
    """
    try:
      t = YANGDynClass(v,base=YANGBool, default=YANGBool("true"), is_leaf=True, yang_name="external-compare-router-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='boolean', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """external_compare_router_id must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, default=YANGBool("true"), is_leaf=True, yang_name="external-compare-router-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='boolean', is_config=False)""",
        })

    self.__external_compare_router_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_external_compare_router_id(self):
    self.__external_compare_router_id = YANGDynClass(base=YANGBool, default=YANGBool("true"), is_leaf=True, yang_name="external-compare-router-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='boolean', is_config=False)


  def _get_advertise_inactive_routes(self):
    """
    Getter method for advertise_inactive_routes, mapped from YANG variable /bgp/peer_groups/peer_group/afi_safis/afi_safi/route_selection_options/state/advertise_inactive_routes (boolean)

    YANG Description: Advertise inactive routes to external peers.  The
default is to only advertise active routes.
    """
    return self.__advertise_inactive_routes
      
  def _set_advertise_inactive_routes(self, v, load=False):
    """
    Setter method for advertise_inactive_routes, mapped from YANG variable /bgp/peer_groups/peer_group/afi_safis/afi_safi/route_selection_options/state/advertise_inactive_routes (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_advertise_inactive_routes is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_advertise_inactive_routes() directly.

    YANG Description: Advertise inactive routes to external peers.  The
default is to only advertise active routes.
    """
    try:
      t = YANGDynClass(v,base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="advertise-inactive-routes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='boolean', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """advertise_inactive_routes must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="advertise-inactive-routes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='boolean', is_config=False)""",
        })

    self.__advertise_inactive_routes = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_advertise_inactive_routes(self):
    self.__advertise_inactive_routes = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="advertise-inactive-routes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='boolean', is_config=False)


  def _get_enable_aigp(self):
    """
    Getter method for enable_aigp, mapped from YANG variable /bgp/peer_groups/peer_group/afi_safis/afi_safi/route_selection_options/state/enable_aigp (boolean)

    YANG Description: Flag to enable sending / receiving accumulated IGP
attribute in routing updates
    """
    return self.__enable_aigp
      
  def _set_enable_aigp(self, v, load=False):
    """
    Setter method for enable_aigp, mapped from YANG variable /bgp/peer_groups/peer_group/afi_safis/afi_safi/route_selection_options/state/enable_aigp (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_enable_aigp is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_enable_aigp() directly.

    YANG Description: Flag to enable sending / receiving accumulated IGP
attribute in routing updates
    """
    try:
      t = YANGDynClass(v,base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="enable-aigp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='boolean', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """enable_aigp must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="enable-aigp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='boolean', is_config=False)""",
        })

    self.__enable_aigp = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_enable_aigp(self):
    self.__enable_aigp = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="enable-aigp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='boolean', is_config=False)


  def _get_ignore_next_hop_igp_metric(self):
    """
    Getter method for ignore_next_hop_igp_metric, mapped from YANG variable /bgp/peer_groups/peer_group/afi_safis/afi_safi/route_selection_options/state/ignore_next_hop_igp_metric (boolean)

    YANG Description: Ignore the IGP metric to the next-hop when calculating
BGP best-path. The default is to select the route for
which the metric to the next-hop is lowest
    """
    return self.__ignore_next_hop_igp_metric
      
  def _set_ignore_next_hop_igp_metric(self, v, load=False):
    """
    Setter method for ignore_next_hop_igp_metric, mapped from YANG variable /bgp/peer_groups/peer_group/afi_safis/afi_safi/route_selection_options/state/ignore_next_hop_igp_metric (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ignore_next_hop_igp_metric is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ignore_next_hop_igp_metric() directly.

    YANG Description: Ignore the IGP metric to the next-hop when calculating
BGP best-path. The default is to select the route for
which the metric to the next-hop is lowest
    """
    try:
      t = YANGDynClass(v,base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="ignore-next-hop-igp-metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='boolean', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ignore_next_hop_igp_metric must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="ignore-next-hop-igp-metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='boolean', is_config=False)""",
        })

    self.__ignore_next_hop_igp_metric = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ignore_next_hop_igp_metric(self):
    self.__ignore_next_hop_igp_metric = YANGDynClass(base=YANGBool, default=YANGBool("false"), is_leaf=True, yang_name="ignore-next-hop-igp-metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/bgp', defining_module='openconfig-bgp', yang_type='boolean', is_config=False)

  always_compare_med = property(_get_always_compare_med)
  ignore_as_path_length = property(_get_ignore_as_path_length)
  external_compare_router_id = property(_get_external_compare_router_id)
  advertise_inactive_routes = property(_get_advertise_inactive_routes)
  enable_aigp = property(_get_enable_aigp)
  ignore_next_hop_igp_metric = property(_get_ignore_next_hop_igp_metric)


  _pyangbind_elements = {'always_compare_med': always_compare_med, 'ignore_as_path_length': ignore_as_path_length, 'external_compare_router_id': external_compare_router_id, 'advertise_inactive_routes': advertise_inactive_routes, 'enable_aigp': enable_aigp, 'ignore_next_hop_igp_metric': ignore_next_hop_igp_metric, }


