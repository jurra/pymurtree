#include "solver_result.h"

class ExportTree {

public:

    /*
     * @brief Export the tree structure in text format
     * @param[in] tree      top node of the tree
     * @param[in] filepath  path to output file, std::cout will be used if not specified 
     */
    static void exportText(MurTree::DecisionNode* tree = nullptr, std::string filepath = "");

    static void exportDOT(MurTree::DecisionNode* tree = nullptr, std::string filepath = "");

private:

    ExportTree(MurTree::DecisionNode* tree, std::ostream* os, bool textformat);

    /*
     * @brief Write the tree structure to m_os
     * @param[in] parentnode    parent node of current edge
     * @param[in] rightedge     true if current edge connects the parent node to its right child node, false otherwise
     * @param[in] indentationlevel      level of indentation
     * @note In MurTree, the right child of a node indicates that the feature is present, the left node indicates the feature is missing
    */
    void writeEdge(MurTree::DecisionNode* parentnode, bool rightedge, unsigned int indentationlevel = 0);
    
    std::ostream* m_os;
    MurTree::DecisionNode* m_tree;    

};